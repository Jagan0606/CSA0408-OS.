# Shortest Job Next (SJN) Scheduling in Python

class Process:
    def __init__(self, pid, bt):
        self.pid = pid    
        self.bt = bt       
        self.wt = 0        
        self.tat = 0       

def sjn_scheduling(processes):
    
    processes.sort(key=lambda x: x.bt)

    
    processes[0].wt = 0
    for i in range(1, len(processes)):
        processes[i].wt = processes[i-1].wt + processes[i-1].bt

  
    for i in range(len(processes)):
        processes[i].tat = processes[i].wt + processes[i].bt

    print("\nProcess\tBT\tWT\tTAT")
    total_wt, total_tat = 0, 0
    for p in processes:
        print(f"P{p.pid}\t{p.bt}\t{p.wt}\t{p.tat}")
        total_wt += p.wt
        total_tat += p.tat

    print(f"\nAverage Waiting Time = {total_wt/len(processes):.2f}")
    print(f"Average Turnaround Time = {total_tat/len(processes):.2f}")


if __name__ == "__main__":
    n = int(input("Enter number of processes: "))
    processes = []
    for i in range(n):
        bt = int(input(f"Enter Burst Time for P{i+1}: "))
        processes.append(Process(i+1, bt))

    sjn_scheduling(processes)
