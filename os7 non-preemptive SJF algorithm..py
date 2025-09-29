 
processes = ['P1', 'P2', 'P3', 'P4']
burst_time = [6, 8, 7, 3]
arrival_time = [2, 5, 1, 0]

# Number of processes
n = len(processes)

# Initialize waiting time and turnaround time lists
waiting_time = [0] * n
turnaround_time = [0] * n

# Combine process info for sorting
process_info = list(zip(processes, arrival_time, burst_time))

process_info.sort(key=lambda x: x[1])

# Calculate completion, waiting, and turnaround times
current_time = 0
completed = []

while process_info:
    # Select processes that have arrived
    available = [p for p in process_info if p[1] <= current_time]
    
    if not available:
        # If no process has arrived, move current time forward
        current_time = process_info[0][1]
        available = [p for p in process_info if p[1] <= current_time]
    
    # Pick process with minimum burst time among available
    next_proc = min(available, key=lambda x: x[2])
    
    idx = process_info.index(next_proc)
    process_info.pop(idx)
    
    # Calculate times
    start_time = current_time
    finish_time = start_time + next_proc[2]
    waiting_time[processes.index(next_proc[0])] = start_time - next_proc[1]
    turnaround_time[processes.index(next_proc[0])] = finish_time - next_proc[1]
    
    current_time = finish_time
    completed.append(next_proc[0])

# Display results
print("Process\tArrival\tBurst\tWaiting\tTurnaround")
for i in range(n):
    print(f"{processes[i]}\t{arrival_time[i]}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

print(f"\nAverage Waiting Time: {sum(waiting_time)/n:.2f}")
print(f"Average Turnaround Time: {sum(turnaround_time)/n:.2f}")
