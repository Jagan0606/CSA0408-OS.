# ls_sim.py
# Simple ls: lists files and folders in current directory
import os
import argparse

def ls(path, show_hidden=False):
    entries = os.listdir(path)
    if not show_hidden:
        entries = [e for e in entries if not e.startswith('.')]
    for e in sorted(entries):
        full = os.path.join(path, e)
        tag = '/' if os.path.isdir(full) else ''
        print(e + tag)

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Simple ls")
    p.add_argument("path", nargs='?', default='.', help="directory to list")
    p.add_argument("-a", "--all", action="store_true", help="show hidden files")
    args = p.parse_args()
    ls(args.path, args.all)
