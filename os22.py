def best_fit(blocks, processes):
    allocation = [-1]*len(processes)
    for i in range(len(processes)):
        best_index = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if best_index == -1 or blocks[j] < blocks[best_index]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            blocks[best_index] -= processes[i]
    return allocation

blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
print("Best Fit Allocation:", best_fit(blocks[:], processes), flush=True)
