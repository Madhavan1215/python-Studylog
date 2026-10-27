import argparse

def cmd_add(args):
    print(f"Adding {args.hours} hours of {args.topic}")

def cmd_list(args):
    print("Listing study logs")

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