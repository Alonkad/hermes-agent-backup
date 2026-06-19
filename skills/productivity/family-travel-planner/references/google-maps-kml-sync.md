# Google My Maps Programmatic Synchronization via KML

Since Google My Maps lacks a public REST API for adding, editing, or deleting features programmatically, we use an automated workaround involving **Network Link KML** files hosted on Google Drive.

## The Sync Architecture

```
[Agent writes data] -> [Python updates KML locally] -> [Upload & Overwrite in Google Drive]
                                                                    | (Direct download URL)
                                                                    v
                                                       [Google My Maps auto-refreshes]
```

## How to Set It Up

1. **Generate the KML Structure:**
   Create a standard KML file containing style mappings and placemark geometries. (See the template below).
2. **Upload to Google Drive:**
   Upload the KML file to Google Drive and set the permission to **Public ("Anyone with link can view")**. This is required so Google Maps can pull the file.
3. **Get the Direct Download URL:**
   Convert the standard Drive viewer URL to a direct-download stream:
   `https://drive.google.com/uc?export=download&id=FILE_ID`
4. **Link to My Maps:**
   - Go to Google My Maps.
   - Click **Import** under a layer.
   - Choose **More** -> **Web URL (Paste URL)** and paste the Direct Download URL.
   - From now on, Google My Maps will periodically auto-refresh the layer by reading this URL.

---

## Python KML Generation Implementation

Here is the helper script used to update the KML file and upload it to Google Drive by over-writing the existing file (preserving its File ID and thus preserving the Sync URL):

```python
import fitz # or other geocoding tools
import json
from googleapiclient.http import MediaFileUpload
from google_api import build_service # Workspace wrapper script

FILE_ID = "1dU6v0SUtgAor6y8zOcs2fOVY-TFKUlB5" # Set the active file ID
LOCAL_KML_PATH = "/tmp/austria_2026.kml"

def update_kml_in_drive(file_id, local_path):
    drive_service = build_service('drive', 'v3')
    
    media = MediaFileUpload(local_path, mimetype='application/vnd.google-earth.kml+xml', resumable=True)
    
    updated_file = drive_service.files().update(
        fileId=file_id,
        media_body=media,
        fields='id, webViewLink'
    ).execute()
    
    return updated_file.get('id')
```

---

## KML Schema Template

Use this template to generate/append placemarks with rich HTML descriptions:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
  <Document>
    <name>Kaduri Family Austria Summer 2026</name>
    <description>קובץ המיקומים המסתנכרן אוטומטית עבור טיול משפחת כדורי לאוסטריה</description>
    <Style id="carStyle">
      <IconStyle>
        <scale>1.2</scale>
        <Icon>
          <href>http://maps.google.com/mapfiles/kml/shapes/car.png</href>
        </Icon>
      </IconStyle>
    </Style>
    <Style id="hotelStyle">
      <IconStyle>
        <scale>1.2</scale>
        <Icon>
          <href>http://maps.google.com/mapfiles/kml/shapes/lodging.png</href>
        </Icon>
      </IconStyle>
    </Style>
    <Placemark>
      <name>איסוף רכב - Budget Germany</name>
      <description><![CDATA[
        <b>ספק מקומי:</b> Budget Germany (דרך אופרן)<br/>
        <b>קוד הזמנה:</b> 75104083 / 46592419IL6<br/>
      ]]></description>
      <styleUrl>#carStyle</styleUrl>
      <Point>
        <coordinates>11.7785925,48.3539625,0</coordinates>
      </Point>
    </Placemark>
  </Document>
</kml>
```
