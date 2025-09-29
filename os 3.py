 
def fcfs(processes, burst_times):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

  
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + burst_times[i-1]

     
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_times[i]


    print("Process\tBurst\tWaiting\tTurnaround")
    for i in range(n):
        print(f"P{processes[i]}\t{burst_times[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

    
    avg_wt = sum(waiting_time) / n
    avg_tat = sum(turnaround_time) / n
    print(f"\nAverage Waiting Time: {avg_wt:.2f}")
    print(f"Average Turnaround Time: {avg_tat:.2f}")

process_ids = [1, 2, 3, 4]
burst_times = [6, 4, 8, 3]
fcfs(process_ids, burst_times)
