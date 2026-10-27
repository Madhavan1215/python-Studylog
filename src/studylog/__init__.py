import argparse
import json
import sys
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
    if args.hours <= 0 or args.hours > 16:
        print("Error: hours must be more than 0 and at most 16.", file=sys.stderr)
        sys.exit(1)

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

def cmd_stats(args):
    sessions = load()
    
    if not sessions:
        print("No study sessions logged yet. Use 'studylog add <topic> <hours>' to log a new session.")
        return
    totals={}


    for s in sessions:
        totals[s["topic"]] = totals.get(s["topic"], 0) + s["hours"]
    
    print(f"{'Topic':<20}{'Hours':>6}")
    for topic, hours in sorted(totals.items(), key=lambda x: x[1], reverse=True):
        print(f"{topic:<20}{hours:>6.1f}")

def cmd_delete(args):
    sessions = load()
    if args.number<1 or args.number>len(sessions):
        print(
            f"Error: no session numbered {args.number}. Run 'studylog list to see the numbers.",
            file=sys.stderr,
        )
        sys.exit(1)

    removed=sessions.pop(args.number -1)
    save(sessions)
    print(f"Deleted: {removed['topic']}, {removed['hours']} hours on {removed['date']}")



def main():
    parser=argparse.ArgumentParser(prog="studylog",description="Track your Sessions")
    subparsers = parser.add_subparsers(dest="command",required=True)

    add_parser = subparsers.add_parser("add" , help="Add a new study log")
    add_parser.add_argument("topic")
    add_parser.add_argument("hours", type=float)
    add_parser.set_defaults(func=cmd_add)

    list_parser= subparsers.add_parser("list" , help="show all study sessions")
    list_parser.set_defaults(func=cmd_list)

    stats_parser= subparsers.add_parser("stats" , help="show total hours per topic")
    stats_parser.set_defaults(func=cmd_stats)

    delete_parser = subparsers.add_parser("delete" ,help="delelte a session from its number ")
    delete_parser.add_argument("number" , type=int)
    delete_parser.set_defaults(func=cmd_delete)



    args = parser.parse_args()
    args.func(args)