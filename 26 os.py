 
#🧾 Simple Python File Manager (Beginner-Friendly)
# Simple File Management Program in Python

# Create a new file
def create_file():
    name = input("Enter file name to create: ")
    with open(name, 'w') as f:
        print(f"✅ File '{name}' created successfully.")

# Write to a file
def write_file():
    name = input("Enter file name to write to: ")
    text = input("Enter text to write: ")
    with open(name, 'a') as f:
        f.write(text + '\n')
        print(f"✍️ Text written to '{name}'.")

# Read a file
def read_file():
    name = input("Enter file name to read: ")
    try:
        with open(name, 'r') as f:
            print("📖 File contents:")
            print(f.read())
    except FileNotFoundError:
        print("❌ File not found.")

# Delete a file
def delete_file():
    import os
    name = input("Enter file name to delete: ")
    if os.path.exists(name):
        os.remove(name)
        print(f"🗑️ File '{name}' deleted.")
    else:
        print("❌ File does not exist.")

# Main menu
def menu():
    while True:
        print("\n📁 File Manager Menu")
        print("1. Create File")
        print("2. Write to File")
        print("3. Read File")
        print("4. Delete File")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            create_file()
        elif choice == '2':
            write_file()
        elif choice == '3':
            read_file()
        elif choice == '4':
            delete_file()
        elif choice == '5':
            print("👋 Exiting program.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

# Run the program
menu()

  

T 
