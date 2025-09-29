import os

# Create a file
with open("sample.txt", "w") as f:
    f.write("ABCDEFG")

# Seek and read
with open("sample.txt", "r") as f:
    f.seek(2)
    print("Seek to pos 2 ->", f.read(3), flush=True)

# File stat
info = os.stat("sample.txt")
print("File size:", info.st_size, "bytes", flush=True)

# Directory read
files = os.listdir(".")
print("Files in current directory:", files, flush=True)

# Cleanup
os.remove("sample.txt")
print("sample.txt deleted", flush=True)
