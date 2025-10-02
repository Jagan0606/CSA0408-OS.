# optimal_paging.py
# Optimal page replacement: replace page that won't be used for longest time
def optimal(pages, frames_count):
    frames = []
    faults = 0
    n = len(pages)
    for i, p in enumerate(pages):
        if p in frames:
            pass
        else:
            faults += 1
            if len(frames) < frames_count:
                frames.append(p)
            else:
                # choose victim: page in frames with farthest next use
                distances = {}
                for f in frames:
                    try:
                        next_use = pages.index(f, i+1)
                    except ValueError:
                        next_use = float('inf')
                    distances[f] = next_use
                victim = max(distances, key=distances.get)
                frames[frames.index(victim)] = p
        print(f"Access {p} -> frames: {frames}")
    print(f"Total page faults: {faults}")

if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3]
    optimal(pages, frames_count=3)
