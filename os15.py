directories = {}

def create_user_dir(user):
    directories[user] = {}
    print(f"Directory for {user} created", flush=True)

def create_file(user, fname, content):
    directories[user][fname] = content
    print(f"File '{fname}' created in {user}", flush=True)

def view_files(user):
    for f, c in directories[user].items():
        print(f, ":", c, flush=True)

# Demo
create_user_dir("Alice")
create_file("Alice", "a.txt", "Hi")
create_user_dir("Bob")
create_file("Bob", "b.txt", "Hello")
view_files("Alice")
view_files("Bob")
