# fifo_paging.py
# Simulate FIFO page replacement. Simple and educational.
def fifo(pages, frames_count):
    frames = []
    pointer = 0
    faults = 0
    for p in pages:
        if p not in frames:
            faults += 1
            if len(frames) < frames_count:
                frames.append(p)
            else:
                frames[pointer] = p
                pointer = (pointer + 1) % frames_count
        print(f"Access {p} -> frames: {frames}")
    print(f"Total page faults: {faults}")

if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
    fifo(pages, frames_count=3)
