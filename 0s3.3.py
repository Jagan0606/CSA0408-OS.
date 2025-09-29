# First Come First Served (FCFS) Scheduling in Python
# Processes and Burst Times are defined inside the program itself

class Process:
    def __init__(self, pid, bt):
        self.pid = pid    # Process ID
        self.bt = bt      # Burst Time
        self.wt = 0       # Waiting Time
        self.tat = 0      # Turnaround Time

def fcfs_scheduling(processes):
    # Waiting time for first process = 0
    processes[0].wt = 0

    # Calculate waiting times
    for i in range(1, len(processes)):
        processes[i].wt = processes[i-1].wt + processes[i-1].bt

    # Calculate turnaround times
    for i in range(len(processes)):
        processes[i].tat = processes[i].wt + processes[i].bt

    # Print results
    print("\nProcess\tBT\tWT\tTAT")
    total_wt, total_tat = 0, 0
    for p in processes:
        print(f"P{p.pid}\t{p.bt}\t{p.wt}\t{p.tat}")
        total_wt += p.wt
        total_tat += p.tat

    print(f"\nAverage Waiting Time = {total_wt/len(processes):.2f}")
    print(f"Average Turnaround Time = {total_tat/len(processes):.2f}")


if __name__ == "__main__":
    # Define processes here (PID, Burst Time)
    processes = [
        Process(1, 5),   # Process 1 with burst time 5
        Process(2, 8),   # Process 2 with burst time 8
        Process(3, 12)   # Process 3 with burst time 12
    ]

    fcfs_scheduling(processes)
