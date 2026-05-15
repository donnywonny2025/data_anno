#!/usr/bin/env python3
"""
DA Session State Engine
=======================
Replaces da_time_tracker.py with full session state management.

Commands:
    start       Start a new session (--project NAME --pay RATE)
    status      Print current session state (call BEFORE every AI response)
    checkpoint  Log a step (--step TYPE --note "description")
    task-done   Increment completed task counter
    stop        End the session and print summary

State file: .tmp/da_session_state.json
"""

import sys
import os
import json
import time
import argparse
from datetime import datetime

# Resolve paths relative to the project root (parent of execution/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
STATE_FILE = os.path.join(PROJECT_ROOT, ".tmp", "da_session_state.json")
OLD_TIMER_FILE = os.path.join(PROJECT_ROOT, ".tmp", "da_session_timer.json")


def _ensure_tmp():
    """Ensure .tmp directory exists."""
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)


def _load_state():
    """Load session state from disk. Returns None if no session."""
    if not os.path.exists(STATE_FILE):
        return None
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return None


def _save_state(state):
    """Write session state to disk."""
    _ensure_tmp()
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def _now_human():
    """Human-readable timestamp."""
    return datetime.now().strftime("%I:%M:%S %p")


def _now_date():
    """Date string for session ID."""
    return datetime.now().strftime("%Y-%m-%d_%H%M%S")


def _elapsed_str(start_epoch):
    """Format elapsed time from epoch to now."""
    elapsed = time.time() - start_epoch
    hours = int(elapsed // 3600)
    minutes = int((elapsed % 3600) // 60)
    seconds = int(elapsed % 60)
    if hours > 0:
        return f"{hours}h {minutes:02d}m {seconds:02d}s"
    else:
        return f"{minutes}m {seconds:02d}s"


def _elapsed_minutes(start_epoch):
    """Return elapsed minutes as float."""
    return (time.time() - start_epoch) / 60.0


def cmd_start(args):
    """Start a new session."""
    # Check for existing active session
    existing = _load_state()
    if existing and existing.get("timer_running"):
        elapsed = _elapsed_str(existing["started_at"])
        print(f"⚠️  SESSION ALREADY RUNNING ({elapsed} on {existing.get('project', 'Unknown')})")
        print(f"   Run 'stop' first to end the current session.")
        sys.exit(1)

    state = {
        "session_id": _now_date(),
        "started_at": time.time(),
        "started_at_human": _now_human(),
        "project": args.project or "Unspecified",
        "pay_rate": args.pay or 0.0,
        "tasks_completed": 0,
        "timer_running": True,
        "checkpoints": [
            {
                "time": _now_human(),
                "epoch": time.time(),
                "step": "session_start",
                "note": f"Started {args.project or 'Unspecified'} session"
            }
        ],
        "stopped_at": None,
        "stopped_at_human": None
    }
    _save_state(state)

    print(f"✅ DA SESSION STARTED")
    print(f"   Project: {state['project']}")
    print(f"   Pay Rate: ${state['pay_rate']:.2f}/hr")
    print(f"   Started: {state['started_at_human']}")
    print(f"   State File: {STATE_FILE}")


def cmd_status(args):
    """Print current session state. This is the critical read-before-respond command."""
    state = _load_state()

    if not state:
        print("═══ DA SESSION STATE ═══")
        print("⚠️  NO ACTIVE SESSION")
        print("   Run: python3 execution/da_session.py start --project \"<name>\" --pay <rate>")
        print("════════════════════════")
        return

    if state.get("timer_running"):
        elapsed = _elapsed_str(state["started_at"])
        timer_label = f"RUNNING | {elapsed} (started {state['started_at_human']})"
        elapsed_min = _elapsed_minutes(state["started_at"])
        earnings = (elapsed_min / 60.0) * state.get("pay_rate", 0)
    else:
        # Session was stopped — show final duration
        if state.get("stopped_at"):
            total_sec = state["stopped_at"] - state["started_at"]
            hours = int(total_sec // 3600)
            minutes = int((total_sec % 3600) // 60)
            seconds = int(total_sec % 60)
            if hours > 0:
                elapsed = f"{hours}h {minutes:02d}m {seconds:02d}s"
            else:
                elapsed = f"{minutes}m {seconds:02d}s"
            timer_label = f"STOPPED | {elapsed} (ended {state['stopped_at_human']})"
            earnings = (total_sec / 3600.0) * state.get("pay_rate", 0)
        else:
            timer_label = "STOPPED"
            earnings = 0

    # Last checkpoint
    last_cp = state.get("checkpoints", [])[-1] if state.get("checkpoints") else None
    if last_cp:
        # Calculate how long ago the last checkpoint was
        cp_epoch = last_cp.get("epoch", 0)
        if cp_epoch:
            ago_sec = time.time() - cp_epoch
            if ago_sec < 60:
                ago_str = f"{int(ago_sec)}s ago"
            elif ago_sec < 3600:
                ago_str = f"{int(ago_sec // 60)}m ago"
            else:
                ago_str = f"{int(ago_sec // 3600)}h {int((ago_sec % 3600) // 60)}m ago"
        else:
            ago_str = "unknown"
        last_step = f"{last_cp.get('step', '?')} | \"{last_cp.get('note', '')}\" | {ago_str}"
    else:
        last_step = "None"

    print("═══ DA SESSION STATE ═══")
    print(f"⏱️  Timer: {timer_label}")
    print(f"📋 Project: {state.get('project', '?')} | ${state.get('pay_rate', 0):.2f}/hr")
    print(f"📊 Tasks: {state.get('tasks_completed', 0)} completed")
    print(f"🔄 Last Step: {last_step}")
    print(f"💰 Est. Earnings: ${earnings:.2f}")
    print("════════════════════════")


def cmd_checkpoint(args):
    """Log a checkpoint. Call after every action."""
    state = _load_state()
    if not state:
        print("⚠️  NO ACTIVE SESSION — cannot checkpoint")
        sys.exit(1)

    step = args.step or "unspecified"
    note = args.note or ""

    checkpoint = {
        "time": _now_human(),
        "epoch": time.time(),
        "step": step,
        "note": note
    }
    state.setdefault("checkpoints", []).append(checkpoint)
    _save_state(state)

    print(f"📌 Checkpoint: [{step}] {note}")


def cmd_task_done(args):
    """Increment completed task counter."""
    state = _load_state()
    if not state:
        print("⚠️  NO ACTIVE SESSION — cannot log task")
        sys.exit(1)

    state["tasks_completed"] = state.get("tasks_completed", 0) + 1
    count = state["tasks_completed"]

    # Also log as checkpoint
    checkpoint = {
        "time": _now_human(),
        "epoch": time.time(),
        "step": "task_done",
        "note": f"Task #{count} completed"
    }
    state.setdefault("checkpoints", []).append(checkpoint)
    _save_state(state)

    print(f"✅ Task #{count} complete | Total: {count}")


def cmd_stop(args):
    """End the session and print summary."""
    state = _load_state()
    if not state:
        print("⚠️  NO ACTIVE SESSION to stop")
        sys.exit(1)

    if not state.get("timer_running"):
        print("⚠️  Session already stopped")
        cmd_status(args)
        return

    state["timer_running"] = False
    state["stopped_at"] = time.time()
    state["stopped_at_human"] = _now_human()

    # Final checkpoint
    checkpoint = {
        "time": _now_human(),
        "epoch": time.time(),
        "step": "session_end",
        "note": "Session ended"
    }
    state.setdefault("checkpoints", []).append(checkpoint)
    _save_state(state)

    # Print summary
    total_sec = state["stopped_at"] - state["started_at"]
    total_min = total_sec / 60.0
    total_hours = total_sec / 3600.0
    earnings = total_hours * state.get("pay_rate", 0)

    hours = int(total_sec // 3600)
    minutes = int((total_sec % 3600) // 60)
    seconds = int(total_sec % 60)

    print("═══ DA SESSION SUMMARY ═══")
    print(f"📋 Project: {state.get('project', '?')}")
    print(f"💵 Pay Rate: ${state.get('pay_rate', 0):.2f}/hr")
    print(f"⏱️  Duration: {hours}h {minutes:02d}m {seconds:02d}s")
    print(f"📊 Tasks Completed: {state.get('tasks_completed', 0)}")
    print(f"💰 Estimated Earnings: ${earnings:.2f}")
    print(f"")
    print(f"⚡ Report {int(total_min)} minutes ({total_hours:.2f} hours) on the DA platform")
    print(f"   Started: {state['started_at_human']}")
    print(f"   Ended: {state['stopped_at_human']}")
    print("══════════════════════════")


def cmd_heartbeat(args):
    """Silent status check for embedding in look.sh output.
    Prints compact status. No error if no session (just prints nothing)."""
    state = _load_state()
    if not state or not state.get("timer_running"):
        # No active session — print nothing (look.sh will just show screenshot paths)
        return

    elapsed = _elapsed_str(state["started_at"])
    elapsed_min = _elapsed_minutes(state["started_at"])
    earnings = (elapsed_min / 60.0) * state.get("pay_rate", 0)

    print("═══ DA SESSION STATE ═══")
    print(f"⏱️  Timer: RUNNING | {elapsed} (started {state['started_at_human']})")
    print(f"📋 Project: {state.get('project', '?')} | ${state.get('pay_rate', 0):.2f}/hr")
    print(f"📊 Tasks: {state.get('tasks_completed', 0)} completed")
    print(f"💰 Est. Earnings: ${earnings:.2f}")
    print("════════════════════════")

    # Auto-checkpoint the screenshot
    checkpoint = {
        "time": _now_human(),
        "epoch": time.time(),
        "step": "screenshot",
        "note": "look.sh heartbeat"
    }
    state.setdefault("checkpoints", []).append(checkpoint)

    # Keep checkpoint list from growing unbounded — trim to last 100
    if len(state["checkpoints"]) > 100:
        state["checkpoints"] = state["checkpoints"][-100:]

    _save_state(state)


def main():
    parser = argparse.ArgumentParser(
        description="DA Session State Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Commands:
  start       Start a new session
  status      Print current state (call BEFORE every AI response)
  checkpoint  Log a step (call AFTER every action)
  task-done   Increment task counter
  stop        End session and print summary
  heartbeat   Silent status for look.sh embedding
        """
    )
    subparsers = parser.add_subparsers(dest="command")

    # start
    p_start = subparsers.add_parser("start", help="Start a new session")
    p_start.add_argument("--project", "-p", type=str, help="Project name")
    p_start.add_argument("--pay", type=float, help="Pay rate ($/hr)")

    # status
    subparsers.add_parser("status", help="Print current session state")

    # checkpoint
    p_cp = subparsers.add_parser("checkpoint", help="Log a checkpoint")
    p_cp.add_argument("--step", "-s", type=str, help="Step type (screenshot, research, draft, etc.)")
    p_cp.add_argument("--note", "-n", type=str, help="Description of what happened")

    # task-done
    subparsers.add_parser("task-done", help="Increment task counter")

    # stop
    subparsers.add_parser("stop", help="End session")

    # heartbeat (used by look.sh)
    subparsers.add_parser("heartbeat", help="Silent status for look.sh")

    args = parser.parse_args()

    if args.command == "start":
        cmd_start(args)
    elif args.command == "status":
        cmd_status(args)
    elif args.command == "checkpoint":
        cmd_checkpoint(args)
    elif args.command == "task-done":
        cmd_task_done(args)
    elif args.command == "stop":
        cmd_stop(args)
    elif args.command == "heartbeat":
        cmd_heartbeat(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
