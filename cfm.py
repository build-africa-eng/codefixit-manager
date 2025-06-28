#!/usr/bin/env python3

import argparse
from cfm.engine.filewalker import collect_files
from cfm.engine.transformer import apply_rules

def main():
    parser = argparse.ArgumentParser(description="CodeFixit Manager CLI")
    parser.add_argument("command", choices=["fix", "dry-run"], help="Action to perform")
    parser.add_argument("--lang", required=True, help="Programming language (e.g. cpp, python)")
    parser.add_argument("--rule", required=True, help="Name of the ruleset (e.g. qt5to6)")
    parser.add_argument("--path", required=True, help="Directory to process")

    args = parser.parse_args()

    rules_path = f"rules/{args.lang}/{args.rule}.json"
    files = collect_files(args.path, args.lang)

    apply_rules(files, rules_path, dry_run=(args.command == "dry-run"))

if __name__ == "__main__":
    main()