import argparse
import json
from pathlib import Path
from datetime import date

DATA_FILE = Path.home() / ".studylog.json"

def load():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE,) as f:
        return json.load(f)

def save(sessions):
    with open(DATA_FILE, "w") as f:
        json.dump(sessions, f, indent=2)

def cmd_add(args):
    sessions= load()
    sessions.append(
        {
            "date": date.today().isoformat(),
            "topic": args.topic,
            "hours": args.hours,
        }
    )
    save(sessions)
    print(f"Logged {args.hours} hours of {args.topic}")

def cmd_list(args):
    sessions = load()
    if not sessions:
        print("No study sessions logged yet. Use 'studylog add <topic> <hours>' to log a new session.")
        return

    print(f"{'#':<4}{'Date':<12}{'Topic':<20}{'Hours':>6}")
    for i, s in enumerate(sessions, start=1):
        print(f"{i:<4}{s['date']:<12}{s['topic']:<20}{s['hours']:>6.1f}")

def main():
    parser=argparse.ArgumentParser(prog="studylog",description="Track your Sessions")
    subparsers = parser.add_subparsers(dest="command",required=True)

    add_parser = subparsers.add_parser("add" , help="Add a new study log")
    add_parser.add_argument("topic")
    add_parser.add_argument("hours", type=float)
    add_parser.set_defaults(func=cmd_add)

    list_parser= subparsers.add_parser("list" , help="show all study sessions")
    list_parser.set_defaults(func=cmd_list)

    args = parser.parse_args()
    args.func(args)