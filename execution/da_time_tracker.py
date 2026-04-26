import time
import os
import json
from datetime import datetime

TRACKER_FILE = ".tmp/da_session_timer.json"

def get_current_time():
    return time.time()

def start_timer():
    data = {
        "start_time": get_current_time(),
        "start_time_human": datetime.now().strftime("%I:%M:%S %p"),
        "tasks_completed": 0
    }
    with open(TRACKER_FILE, "w") as f:
        json.dump(data, f)
    print(f"⏱️ DA Session Timer Started at: {data['start_time_human']}")

def check_timer():
    if not os.path.exists(TRACKER_FILE):
        print("No active timer. Start one with --start")
        return
    
    with open(TRACKER_FILE, "r") as f:
        data = json.load(f)
    
    elapsed_seconds = get_current_time() - data["start_time"]
    minutes = int(elapsed_seconds // 60)
    seconds = int(elapsed_seconds % 60)
    
    print(f"⏱️ Current Session Time: {minutes} minutes, {seconds} seconds")
    print(f"Started at: {data['start_time_human']}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--start":
        start_timer()
    else:
        check_timer()
