def first_fit(blocks, processes):
    allocation = [-1]*len(processes)
    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break
    return allocation

blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
print("First Fit Allocation:", first_fit(blocks[:], processes), flush=True)
