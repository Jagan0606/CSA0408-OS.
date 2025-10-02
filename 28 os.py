# grep_sim.py
# Simple grep: search for pattern in files or stdin
import argparse
import sys

def grep(pattern, files):
    for fname in files or []:
        try:
            with open(fname, 'r', errors='ignore') as f:
                for lineno, line in enumerate(f, 1):
                    if pattern in line:
                        print(f"{fname}:{lineno}:{line.rstrip()}")
        except FileNotFoundError:
            print(f"grep: {fname}: No such file")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern", help="pattern to search")
    parser.add_argument("files", nargs="*", help="files to search (optional)")
    args = parser.parse_args()

    if args.files:
        grep(args.pattern, args.files)
    else:
        # read from stdin
        for lineno, line in enumerate(sys.stdin, 1):
            if args.pattern in line:
                print(f"{lineno}:{line.rstrip()}")
