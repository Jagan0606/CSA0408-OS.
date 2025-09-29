# Non-preemptive Shortest Job First (SJF) Scheduling

# Input: Number of processes
n = int(input("Enter number of processes: "))

processes = []
for i in range(n):
    bt = int(input(f"Enter Burst Time for Process P{i+1}: "))
    processes.append([i+1, bt])  # [Process_ID, Burst_Time]

# Sort by burst time (Shortest Job First)
processes.sort(key=lambda x: x[1])

waiting_time = [0] * n
turnaround_time = [0] * n

# Calculate Waiting Time
for i in range(1, n):
    waiting_time[i] = waiting_time[i-1] + processes[i-1][1]

# Calculate Turnaround Time = Waiting + Burst
for i in range(n):
    turnaround_time[i] = waiting_time[i] + processes[i][1]

# Print results
print("\nProcess\tBurst Time\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"P{processes[i][0]}\t{processes[i][1]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

# Average times
avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n
print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
