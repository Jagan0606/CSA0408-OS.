import threading
import time

def philosopher(name, left_fork, right_fork):
    while True:
        print(f"{name} is thinking", flush=True)
        time.sleep(1)

        # pick up forks
        with left_fork, right_fork:
            print(f"{name} is eating", flush=True)
            time.sleep(2)
        print(f"{name} finished eating", flush=True)

if __name__ == "__main__":
    forks = [threading.Lock() for _ in range(5)]
    names = ["P1", "P2", "P3", "P4", "P5"]

    philosophers = []
    for i in range(5):
        t = threading.Thread(target=philosopher,
                             args=(names[i], forks[i], forks[(i+1)%5]))
        philosophers.append(t)
        t.start()
