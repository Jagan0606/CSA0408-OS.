# cscan_disk.py
# C-SCAN: service in one direction; when end reached jump to other end without servicing on return.
def cscan(requests, start, disk_size=199):
    requests = sorted(requests)
    left = [r for r in requests if r < start]
    right = [r for r in requests if r >= start]
    total = 0
    position = start
    sequence = []

    for r in right:
        sequence.append(r)
        total += abs(position - r)
        position = r
    # go to end
    total += abs(position - disk_size)
    position = 0  # jump to start (no servicing counted for jump)
    # service from beginning up to left
    for r in left:
        sequence.append(r)
        total += abs(position - r)
        position = r

    print("Service order:", sequence)
    print("Total head movement (including end-to-start move):", total)

if __name__ == "__main__":
    reqs = [98, 183, 37, 122, 14, 124, 65, 67]
    cscan(reqs, start=53, disk_size=199)
