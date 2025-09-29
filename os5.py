# Priority Scheduling (Non-Preemptive) - User Input

class Process:
    def __init__(self, pid, bt, priority):
        self.pid = pid            # Process ID
        self.bt = bt              # Burst Time
        self.priority = priority  # Priority
        self.wt = 0               # Waiting Time
        self.tat = 0              # Turnaround Time

def priority_scheduling(processes):
    # Sort processes by priority (lower number = higher priority)
    processes.sort(key=lambda x: x.priority)

    # Calculate waiting time
    processes[0].wt = 0
    for i in range(1, len(processes)):
        processes[i].wt = processes[i-1].wt + processes[i-1].bt

    # Calculate turnaround time
    for i in range(len(processes)):
        processes[i].tat = processes[i].wt + processes[i].bt

    # Display results
    print("\nProcess\tBT\tPriority\tWT\tTAT")
    total_wt, total_tat = 0, 0
    for p in processes:
        print(f"P{p.pid}\t{p.bt}\t{p.priority}\t\t{p.wt}\t{p.tat}")
        total_wt += p.wt
        total_tat += p.tat

    print(f"\nAverage Waiting Time = {total_wt/len(processes):.2f}")
    print(f"Average Turnaround Time = {total_tat/len(processes):.2f}")


if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    processes = []
    for i in range(n):
        bt = int(input(f"Enter Burst Time for P{i+1}: "))
        pr = int(input(f"Enter Priority for P{i+1} (lower = higher priority): "))
        processes.append(Process(i+1, bt, pr))

    priority_scheduling(processes)
