import subprocess
import json
import os

video_path = "/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/documents/L'Enfant_Plaza_escalator_violinist.webm"
wav_path = ".tmp/audio.wav"

# Extract audio
subprocess.run(['ffmpeg', '-y', '-i', video_path, '-vn', '-acodec', 'pcm_s16le', '-ar', '44100', '-ac', '1', wav_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

import wave
import struct
import math

with wave.open(wav_path, 'r') as wav_file:
    frames = wav_file.getnframes()
    rate = wav_file.getframerate()
    duration = frames / float(rate)
    
    # Read in chunks of 1 second
    chunk_size = rate
    volumes = []
    
    for i in range(int(duration)):
        data = wav_file.readframes(chunk_size)
        samples = struct.unpack(f"<{len(data)//2}h", data)
        # Calculate RMS for this second
        rms = math.sqrt(sum(float(s)**2 for s in samples) / len(samples))
        volumes.append(rms)

print(f"Video Duration: {duration:.2f} seconds")
print("Volume analysis over time (1 second intervals):")
for i, v in enumerate(volumes):
    if i % 5 == 0:
        print(f"Sec {i:02d}: {'*' * int(v / 500)} ({int(v)})")

os.remove(wav_path)
