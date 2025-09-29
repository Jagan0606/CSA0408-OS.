 
from multiprocessing import Process, Value
import time

 
def increment(shared_num):
    for _ in range(5):
        with shared_num.get_lock():   
            shared_num.value += 1
            print("Child Process incremented value to:", shared_num.value)
        time.sleep(1)

if __name__ == "__main__":
    # Create shared memory (an integer with initial value 0)
    number = Value('i', 0)   # 'i' means integer

    # Create child process
    p = Process(target=increment, args=(number,))
    p.start()

    # Parent process also modifies the same shared memory
    for _ in range(5):
        with number.get_lock():
            number.value += 10
            print("Parent Process added 10, value is:", number.value)
        time.sleep(1)

    p.join()

    print("\nFinal value in shared memory:", number.value)
