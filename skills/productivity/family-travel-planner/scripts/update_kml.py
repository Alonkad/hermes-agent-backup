#!/usr/bin/env python3
"""
Update Google My Maps KML backend for Kaduri Family Travel Planner.

This script parses and appends new locations (placemarks) to the shared KML file
located on Google Drive (File ID: 1dU6v0SUtgAor6y8zOcs2fOVY-TFKUlB5).
The KML is shared with the user and loaded into Google My Maps via 'Shared with me' Drive import.
"""

import sys
import os
import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path

# Ensure google-workspace skill scripts are importable
GW_SCRIPTS = Path(os.path.expanduser('~/.hermes/skills/productivity/google-workspace/scripts'))
if GW_SCRIPTS.exists() and str(GW_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(GW_SCRIPTS))

try:
    from google_api import build_service
    from googleapiclient.http import MediaFileUpload
except ImportError:
    print("Error: google-workspace skill dependencies not found. Please ensure it is set up.", file=sys.stderr)
    sys.exit(1)

KML_FILE_ID = "1dU6v0SUtgAor6y8zOcs2fOVY-TFKUlB5"

def get_kml_content(drive_service):
    """Download current KML content from Google Drive."""
    import io
    from googleapiclient.http import MediaIoBaseDownload
    request = drive_service.files().get_media(fileId=KML_FILE_ID)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
         _, done = downloader.next_chunk()
    return fh.getvalue().decode('utf-8')

def upload_kml_content(drive_service, kml_content, local_temp_path='/tmp/austria_2026.kml'):
    """Upload KML content, overwriting the file on Google Drive."""
    with open(local_temp_path, 'w', encoding='utf-8') as f:
        f.write(kml_content)
    
    media = MediaFileUpload(local_temp_path, mimetype='application/vnd.google-earth.kml+xml', resumable=True)
    drive_service.files().update(
        fileId=KML_FILE_ID,
        media_body=media,
        fields='id'
    ).execute()

def add_placemark(kml_text, name, description, lat, lon, style_id="hotelStyle"):
    """Parse KML, insert new placemark, and serialize back to string."""
    # Register namespaces to prevent 'ns0:' prefixing
    ET.register_namespace('', "http://www.opengis.net/kml/2.2")
    
    # Simple XML injection or ElementTree parsing
    # Since ElementTree parsing can sometimes stripes CDATA / namespaces details,
    # let's do a reliable insertion before </Document>
    placemark_xml = f"""    <Placemark>
      <name>{name}</name>
      <description><![CDATA[{description}]]></description>
      <styleUrl>#{style_id}</styleUrl>
      <Point>
        <coordinates>{lon},{lat},0</coordinates>
      </Point>
    </Placemark>
"""
    
    end_doc_idx = kml_text.rfind("</Document>")
    if end_doc_idx == -1:
        raise ValueError("Invalid KML format: </Document> not found")
        
    updated_kml = kml_text[:end_doc_idx] + placemark_xml + "    " + kml_text[end_doc_idx:]
    return updated_kml

def main():
    parser = argparse.ArgumentParser(description="Add locations to Kaduri Austria Trip KML on Google Drive.")
    parser.add_argument("--name", required=True, help="Name of the place")
    parser.add_argument("--description", required=True, help="HTML Description (CDATA) for details")
    parser.add_argument("--lat", type=float, required=True, help="Latitude")
    parser.add_argument("--lon", type=float, required=True, help="Longitude")
    parser.add_argument("--style", default="hotelStyle", choices=["hotelStyle", "carStyle", "genericStyle"], help="Style ID to use")
    
    args = parser.parse_args()
    
    drive_service = build_service('drive', 'v3')
    
    print(f"Fetching current KML from Drive (ID: {KML_FILE_ID})...")
    current_kml = get_kml_content(drive_service)
    
    if name_already_exists(current_kml, args.name):
        print(f"Warning: Placemark '{args.name}' already exists in KML. Skipping update to avoid duplicate.")
        sys.exit(0)
        
    print(f"Adding placemark: {args.name} ({args.lat}, {args.lon})...")
    updated_kml = add_placemark(current_kml, args.name, args.description, args.lat, args.lon, args.style)
    
    print("Uploading updated KML back to Google Drive...")
    upload_kml_content(drive_service, updated_kml)
    print("SUCCESS: Google My Maps (KML Layer) updated successfully!")

def name_already_exists(kml_text, name):
    return f"<name>{name}</name>" in kml_text

if __name__ == '__main__':
    main()
