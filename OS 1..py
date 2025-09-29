import os
import multiprocessing

def child_process():
    print("\n--- Child Process ---")
    print("Child PID:", os.getpid())
    print("Parent PID (PPID):", os.getppid())

def main():
    print("\n--- Parent Process ---")
    print("Parent PID:", os.getpid())

   
    p = multiprocessing.Process(target=child_process)
    p.start()
    print("Child PID (from parent):", p.pid)

    p.join()   

if __name__ == "__main__":  
    main()

