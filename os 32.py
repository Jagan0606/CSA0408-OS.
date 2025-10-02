# lru_paging.py
# Simple LRU using list ordering: most recently used at end
def lru(pages, frames_count):
    frames = []
    faults = 0
    for p in pages:
        if p in frames:
            # move to most recently used
            frames.remove(p)
            frames.append(p)
        else:
            faults += 1
            if len(frames) < frames_count:
                frames.append(p)
            else:
                frames.pop(0)  # remove least recently used (front)
                frames.append(p)
        print(f"Access {p} -> frames: {frames}")
    print(f"Total page faults: {faults}")

if __name__ == "__main__":
    pages = [1,2,3,2,4,1,5,2,1,2,3,4]
    lru(pages, frames_count=3)
