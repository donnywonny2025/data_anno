#!/bin/bash
# DA Work Timer — always logs to the same place
# Usage: ./execution/timer.sh start    → begins timing
#        ./execution/timer.sh stop     → stops, logs to shift log
#        ./execution/timer.sh status   → shows elapsed time

TIMER_FILE="/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/.tmp/timer_state"
LOG_DIR="/Volumes/WORK 2TB/WORK 2026/DATA_ANNOTATION/war_room/TASK_LOG"
mkdir -p "$(dirname "$TIMER_FILE")"
mkdir -p "$LOG_DIR"

case "$1" in
  start)
    if [ -f "$TIMER_FILE" ]; then
      echo "⚠️  Timer already running!"
      START=$(cat "$TIMER_FILE")
      NOW=$(date +%s)
      ELAPSED=$(( NOW - START ))
      HOURS=$(( ELAPSED / 3600 ))
      MINS=$(( (ELAPSED % 3600) / 60 ))
      echo "⏱️  Running for: ${HOURS}h ${MINS}m"
      exit 1
    fi
    date +%s > "$TIMER_FILE"
    START_TIME=$(date "+%I:%M %p")
    echo "✅ Timer started at $START_TIME"
    echo "   Run './execution/timer.sh status' to check elapsed time"
    echo "   Run './execution/timer.sh stop' when done"
    ;;

  stop)
    if [ ! -f "$TIMER_FILE" ]; then
      echo "❌ No timer running."
      exit 1
    fi
    START=$(cat "$TIMER_FILE")
    NOW=$(date +%s)
    ELAPSED=$(( NOW - START ))
    HOURS=$(( ELAPSED / 3600 ))
    MINS=$(( (ELAPSED % 3600) / 60 ))
    TOTAL_HOURS=$(echo "scale=2; $ELAPSED / 3600" | bc)
    
    START_TIME=$(date -r "$START" "+%I:%M %p")
    STOP_TIME=$(date "+%I:%M %p")
    TODAY=$(date "+%Y%m%d")
    LOG_FILE="$LOG_DIR/da_shift_log_${TODAY}.md"

    # Append to today's shift log
    if [ ! -f "$LOG_FILE" ]; then
      echo "# DA Shift Log — $(date '+%B %d, %Y')" > "$LOG_FILE"
      echo "" >> "$LOG_FILE"
    fi

    echo "" >> "$LOG_FILE"
    echo "## Session: $START_TIME → $STOP_TIME" >> "$LOG_FILE"
    echo "- **Duration:** ${HOURS}h ${MINS}m (${TOTAL_HOURS} hours)" >> "$LOG_FILE"
    echo "- **Projects:** " >> "$LOG_FILE"
    echo "- **Rate:** \$/hr" >> "$LOG_FILE"
    echo "- **Earnings:** \$" >> "$LOG_FILE"
    echo "- **Notes:** " >> "$LOG_FILE"

    rm "$TIMER_FILE"

    echo "⏹️  Timer stopped."
    echo "   Session: $START_TIME → $STOP_TIME"
    echo "   Duration: ${HOURS}h ${MINS}m ($TOTAL_HOURS hours)"
    echo "   📝 Logged to: $LOG_FILE"
    echo ""
    echo "   ⚠️  Don't forget to REPORT HOURS on the DA platform!"
    ;;

  status)
    if [ ! -f "$TIMER_FILE" ]; then
      echo "❌ No timer running."
      exit 1
    fi
    START=$(cat "$TIMER_FILE")
    NOW=$(date +%s)
    ELAPSED=$(( NOW - START ))
    HOURS=$(( ELAPSED / 3600 ))
    MINS=$(( (ELAPSED % 3600) / 60 ))
    SECS=$(( ELAPSED % 60 ))
    START_TIME=$(date -r "$START" "+%I:%M %p")
    echo "⏱️  Timer running since $START_TIME"
    echo "   Elapsed: ${HOURS}h ${MINS}m ${SECS}s"
    ;;

  *)
    echo "Usage: ./execution/timer.sh [start|stop|status]"
    ;;
esac
