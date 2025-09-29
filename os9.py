import multiprocessing

def child_process(shared_value, shared_array):
    print("\n--- Child Process ---")
    
    # Read from shared memory
    print("Child reads shared_value:", shared_value.value)
    print("Child reads shared_array:", list(shared_array))
    
    # Modify the shared memory
    shared_value.value += 10
    for i in range(len(shared_array)):
        shared_array[i] += 1

    print("Child modified shared_value to:", shared_value.value)
    print("Child modified shared_array to:", list(shared_array))


def main():
    # Create shared memory
    shared_value = multiprocessing.Value('i', 100)   # integer value
    shared_array = multiprocessing.Array('i', [1, 2, 3, 4, 5])  # integer array

    print("\n--- Parent Process ---")
    print("Initial shared_value:", shared_value.value)
    print("Initial shared_array:", list(shared_array))

    # Create child process
    p = multiprocessing.Process(target=child_process, args=(shared_value, shared_array))
    p.start()
    p.join()

    # Parent reads after child modified
    print("\n--- Parent Process After Child ---")
    print("shared_value now:", shared_value.value)
    print("shared_array now:", list(shared_array))


if __name__ == "__main__":
    main()
