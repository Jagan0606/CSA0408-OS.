# Simple Round Robin Scheduling (No Arrival Time)

processes = ['P1', 'P2', 'P3']
burst_time = [5, 7, 4]   # Burst times for each process
quantum = 2              # Time quantum

n = len(processes)
waiting_time = [0] * n
turnaround_time = [0] * n
rem_bt = burst_time[:]   # Remaining burst times
time = 0

# Loop until all processes finish
while True:
    done = True
    for i in range(n):
        if rem_bt[i] > 0:
            done = False  # There is a process still running
            if rem_bt[i] > quantum:
                time += quantum
                rem_bt[i] -= quantum
            else:
                time += rem_bt[i]
                waiting_time[i] = time - burst_time[i]
                rem_bt[i] = 0
    if done:
        break

# Calculate Turnaround Time
for i in range(n):
    turnaround_time[i] = waiting_time[i] + burst_time[i]

# Print results
print("Process\tBT\tWT\tTAT")
for i in range(n):
    print(f"{processes[i]}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

print("\nAverage Waiting Time:", sum(waiting_time)/n)
print("Average Turnaround Time:", sum(turnaround_time)/n)
