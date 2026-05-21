#!/bin/bash
# DA Task Timer — tracks start/stop/elapsed for every task
# Usage:
#   task_timer.sh start "MORT-51426.2"   → logs start time
#   task_timer.sh stop                    → logs stop time, prints elapsed
#   task_timer.sh status                  → prints current elapsed time
#   task_timer.sh log                     → shows full history

TIMER_FILE="/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/.task_timer"
LOG_FILE="/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/time_log.csv"

# Initialize log file with header if it doesn't exist
if [ ! -f "$LOG_FILE" ]; then
    echo "task_id,start_time,stop_time,elapsed_minutes,date" > "$LOG_FILE"
fi

case "$1" in
    start)
        TASK_ID="${2:-UNKNOWN}"
        START=$(date +%s)
        START_HUMAN=$(date "+%Y-%m-%d %H:%M:%S")
        echo "${TASK_ID}|${START}|${START_HUMAN}" > "$TIMER_FILE"
        echo "⏱  Timer started for ${TASK_ID} at ${START_HUMAN}"
        ;;
    stop)
        if [ ! -f "$TIMER_FILE" ]; then
            echo "❌ No timer running. Start one with: task_timer.sh start TASK-ID"
            exit 1
        fi
        IFS='|' read -r TASK_ID START START_HUMAN < "$TIMER_FILE"
        STOP=$(date +%s)
        STOP_HUMAN=$(date "+%Y-%m-%d %H:%M:%S")
        ELAPSED=$(( (STOP - START) / 60 ))
        HOURS=$(( ELAPSED / 60 ))
        MINS=$(( ELAPSED % 60 ))
        echo "${TASK_ID},${START_HUMAN},${STOP_HUMAN},${ELAPSED},$(date +%Y-%m-%d)" >> "$LOG_FILE"
        rm "$TIMER_FILE"
        echo "⏱  Timer stopped for ${TASK_ID}"
        echo "   Started:  ${START_HUMAN}"
        echo "   Stopped:  ${STOP_HUMAN}"
        echo "   Elapsed:  ${HOURS}h ${MINS}m (${ELAPSED} minutes total)"
        ;;
    status)
        if [ ! -f "$TIMER_FILE" ]; then
            echo "❌ No timer running."
            exit 1
        fi
        IFS='|' read -r TASK_ID START START_HUMAN < "$TIMER_FILE"
        NOW=$(date +%s)
        ELAPSED=$(( (NOW - START) / 60 ))
        HOURS=$(( ELAPSED / 60 ))
        MINS=$(( ELAPSED % 60 ))
        echo "⏱  ${TASK_ID} — running for ${HOURS}h ${MINS}m (started ${START_HUMAN})"
        ;;
    log)
        if [ -f "$LOG_FILE" ]; then
            column -t -s',' "$LOG_FILE"
        else
            echo "No time log yet."
        fi
        ;;
    *)
        echo "Usage: task_timer.sh {start TASK-ID|stop|status|log}"
        ;;
esac
