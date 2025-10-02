# fcfs_disk.py
# FCFS: service requests in arrival order
def fcfs(requests, start):
    position = start
    total = 0
    print(f"Start at {start}")
    for r in requests:
        move = abs(r - position)
        total += move
        print(f"Move from {position} to {r} -> {move}")
        position = r
    print(f"Total head movement: {total}")

if __name__ == "__main__":
    reqs = [98, 183, 37, 122, 14, 124, 65, 67]
    fcfs(reqs, start=53)
