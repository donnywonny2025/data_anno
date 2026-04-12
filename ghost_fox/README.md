# Ghost Fox Stealth Browser

A modular, persistent stealth automation framework built on Camoufox and Playwright.

## Running Tally of Automation Components
- **Server Core:** `src/server.py` handles Playwright profiles and network routing.
- **Human Emulation:** `src/stealth.py` mimics organic typing and cursor movements.
- **Action Bridge:** `execution/current_command.py` allows real-time async DOM control.
- **Data Scrubbing:** `scrub_momo.py` and `anonymize_local.py` for securing local artifacts.
- **Subagent Bridge:** Active integration with `antigravity` agents.

## Structure
- `src/server.py`: Persistent browser manager.
- `src/stealth.py`: Human-like interaction library (mouse/keyboard).
- `execution/current_command.py`: Bridge file for real-time control.
- `data/screenshots/`: Visual verification logs.

## Usage
1. Start the server:
   ```bash
   python3 src/server.py
   ```
2. Write Python commands to `execution/current_command.py`. The server will execute them immediately on the active page.

## Key Features
- **Persistence**: Browser stays open indefinitely.
- **Stealth**: Hardened against fingerprinting and behavioral analysis.
- **Dynamic Control**: Script-free command bridge.
