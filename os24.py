import os

# Create file
with open("demo.txt", "w") as f:
    f.write("Hello OS")

# Read file
with open("demo.txt", "r") as f:
    print("File content:", f.read(), flush=True)

# Rename file
os.rename("demo.txt", "new_demo.txt")
print("File renamed to new_demo.txt", flush=True)

# Delete file
os.remove("new_demo.txt")
print("File deleted", flush=True)
