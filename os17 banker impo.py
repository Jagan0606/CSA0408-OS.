def is_safe(alloc, max_need, avail):
    n = len(alloc)
    m = len(avail)
    need = [[max_need[i][j]-alloc[i][j] for j in range(m)] for i in range(n)]
    finish = [0]*n
    safe_seq = []
    work = avail[:]

    while len(safe_seq) < n:
        found = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for k in range(m):
                    work[k] += alloc[i][k]
                safe_seq.append(i)
                finish[i] = 1
                found = True
        if not found:
            return False, []
    return True, safe_seq

alloc = [[0,1,0],[2,0,0],[3,0,2],[2,1,1],[0,0,2]]
max_need = [[7,5,3],[3,2,2],[9,0,2],[2,2,2],[4,3,3]]
avail = [3,3,2]

safe, seq = is_safe(alloc, max_need, avail)
print("Safe?", safe, flush=True)
print("Safe Sequence:", seq, flush=True)
