---
name: gaming-and-emulation
description: "Deploys, configures, and operates game servers (Minecraft) and headless emulation setups (Pokemon / PyBoy)."
version: 1.0.0
author: Hermes Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [gaming, minecraft, server, neoforge, forge, modpack, emulator, pokemon, pyboy, raw-reads]
    category: gaming
---

# Gaming and Emulation Playbook

A unified class-level playbook for hosting, monitoring, and operating game servers (such as modded Minecraft setups) and running headless emulator agents (such as Pokemon/PyBoy).

---

## 1. Minecraft Modpack Server Hosting & Config

Operate modded Minecraft servers (CurseForge, Modrinth) using custom Java runtimes, tuned garbage collection (G1GC), and automated backups.

### Initial Preferences Checklist
Before spawning local instances or editing server files, establish preferences:
- **Server Name & MOTD**
- **Difficulty** (peaceful / easy / normal / hard)
- **Gamemode** (survival / creative / adventure)
- **Online Mode** (true/false) — false allows cracked/LAN-friendly offline authentication.
- **View distance & simulation distance** (scaled to hardware specs)
- **RAM allocation ceiling**

### Installation & Initialization
1. **Download and Expand Pack:**
   ```bash
   mkdir -p ~/minecraft-server/server
   cd ~/minecraft-server
   wget -O serverpack.zip "<URL>"
   unzip -o serverpack.zip -d server
   ```
2. **Install Matching Java Runtime:**
   - Minecraft 1.21+ → Java 21: `sudo apt install openjdk-21-jre-headless`
   - Minecraft 1.18-1.20 → Java 17: `sudo apt install openjdk-17-jre-headless`
   - Minecraft 1.16 and below → Java 8: `sudo apt install openjdk-8-jre-headless`
3. **Accept EULA:**
   ```bash
   echo "eula=true" > ~/minecraft-server/server/eula.txt
   ```

### JVM Garbage Collection & Scaling (G1GC Tuning)
Inject optimized GC flags inside `user_jvm_args.txt`. Modded servers require significant RAM offsets (e.g. 6-12GB for medium packs, 12-24GB for large monorepos with 350+ mods).
```
-Xms12G
-Xmx24G
-XX:+UseG1GC
-XX:+ParallelRefProcEnabled
-XX:MaxGCPauseMillis=200
-XX:+UnlockExperimentalVMOptions
-XX:+DisableExplicitGC
-XX:+AlwaysPreTouch
-XX:G1NewSizePercent=30
-XX:G1MaxNewSizePercent=40
-XX:G1HeapRegionSize=8M
-XX:G1ReservePercent=20
-XX:G1HeapWastePercent=5
-XX:G1MixedGCCountTarget=4
-XX:InitiatingHeapOccupancyPercent=15
-XX:G1MixedGCLiveThresholdPercent=90
-XX:G1RSetUpdatingPauseTimePercent=5
-XX:SurvivorRatio=32
-XX:+PerfDisableSharedMem
-XX:MaxTenuringThreshold=1
```

### Automated Backup Pipeline
Create recurring compressed snapshot scripts (`backup.sh`):
```bash
#!/bin/bash
SERVER_DIR="$HOME/minecraft-server/server"
BACKUP_DIR="$HOME/minecraft-server/backups"
WORLD_DIR="$SERVER_DIR/world"
MAX_BACKUPS=24
mkdir -p "$BACKUP_DIR"
[ ! -d "$WORLD_DIR" ] && echo "[BACKUP] No world folder" && exit 0
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
BACKUP_FILE="$BACKUP_DIR/world_${TIMESTAMP}.tar.gz"
tar -czf "$BACKUP_FILE" -C "$SERVER_DIR" world
```
Schedule via hourly system boundaries:
```bash
(crontab -l 2>/dev/null | grep -v "minecraft/backup.sh"; echo "0 * * * * $HOME/minecraft-server/backup.sh >> $HOME/minecraft-server/backups/backup.log 2>&1") | crontab -
```

---

## 2. Headless Emulation & Interactive Gaming (Pokemon / PyBoy)

Programmatically interact with and control emulator layers using memory reading APIs, visual rendering validation loops, and dynamic proxy dashboards.

### Startup Pipeline
1. **Initialize virtual environment** (using python 3.10+ and UV for high-performance dependency resolutions). Note: Roman ROM files `.gb`, `.gbc`, or `.gba` must be provided directly by the user. Do not distribute copyrighted ROMs.
2. **Launch game server endpoint:**
   ```bash
   pokemon-agent serve --rom path/to/rom.gb --port 9876 &
   ```
3. **Establish reverse interface tunnels:**
   To expose visual monitoring dashboards to users on external environments, forge a tunnel via localhost.run:
   ```bash
   ssh -R 80:localhost:9876 nokey@localhost.run
   ```

### Execution Strategy Loops
- **Observe, Orient, Decide, Act (OODA) loop:**
  1. **Observe:** Call `GET /state` to retrieve precise numbers (HP, battle state, maps etc.). Parallelly download `GET /screenshot` and request visual telemetry verification via `vision_analyze`.
  2. **Orient:** Detect transitions (such as doors or stairs) and append 2-3 `wait_60` steps to avoid black screen transitions from reporting stale telemetry.
  3. **Act:** Restrict action arrays to 2-4 movement step iterations (e.g. `walk_up`, `walk_right`, `press_a`) to prevent overshooting or hitting navigation hazards (ledges, building traps).
- **Building Safety Sidestep:** After spawning or exiting a building doorway, never walk directly north or you will instantly step back inside. Sidestep 2 tiles left or right first.
- **Gym Progression Savepoints:** Issue `POST /save` before all risk boundaries: GYM battles, map updates, or major fights.
