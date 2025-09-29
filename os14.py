directory = {}

def create_file(name, content):
    directory[name] = content
    print(f"File '{name}' created", flush=True)

def view_files():
    for name, content in directory.items():
        print(name, ":", content, flush=True)

# Demo
create_file("a.txt", "Hello")
create_file("b.txt", "World")
view_files()
