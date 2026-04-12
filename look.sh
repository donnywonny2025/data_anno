#!/bin/bash

# Define the target directory
DIR="/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/screenshots"
mkdir -p "$DIR"

# Generate a timestamped filename for versioning
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
RAW_FILENAME="$DIR/da_mirror_$TIMESTAMP.jpg"

# 1. Take a silent (-x) screenshot of the main monitor (-m) in JPEG format (-t jpg)
screencapture -x -m -t jpg "$RAW_FILENAME"

# Print the final path for the AI to ingest
echo "$RAW_FILENAME"
