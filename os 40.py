# permissions_demo.py
# Shows permission bits for a given file and explains owner/group/other
import os
import stat
import argparse

def perm_string(mode):
    is_dir = 'd' if stat.S_ISDIR(mode) else '-'
    perms = []
    mapping = [(stat.S_IRUSR, 'r'), (stat.S_IWUSR, 'w'), (stat.S_IXUSR, 'x'),
               (stat.S_IRGRP, 'r'), (stat.S_IWGRP, 'w'), (stat.S_IXGRP, 'x'),
               (stat.S_IROTH, 'r'), (stat.S_IWOTH, 'w'), (stat.S_IXOTH, 'x')]
    for bit, ch in mapping:
        perms.append(ch if (mode & bit) else '-')
    return is_dir + ''.join(perms)

def explain():
    print("Linux permission model (three classes):")
    print("  owner (user) : permissions for file owner")
    print("  group        : permissions for users in owner's group")
    print("  others       : everyone else")
    print("Permission chars: r (read), w (write), x (execute)\n")
    print("Examples of types of users:")
    print("  root (superuser) - can override permissions")
    print("  regular user - may be owner or member of group")
    print("  group members - users who share group with file owner\n")

def show(path):
    st = os.stat(path)
    print("File:", path)
    print("Mode (octal):", oct(st.st_mode & 0o777))
    print("Permissions:", perm_string(st.st_mode))
    print("Owner uid:", st.st_uid, "Group gid:", st.st_gid)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=".", help="file or directory path")
    args = parser.parse_args()
    explain()
    show(args.path)
