import threading
import time

# Semaphore for resource
resource = threading.Semaphore(1)

def reader(id):
    while True:
        resource.acquire()
        print(f"Reader {id} is reading", flush=True)
        resource.release()
        time.sleep(1)

def writer(id):
    while True:
        resource.acquire()
        print(f"Writer {id} is writing", flush=True)
        time.sleep(1)
        resource.release()
        time.sleep(1)

if __name__ == "__main__":
    # Start 2 readers and 1 writer
    threading.Thread(target=reader, args=(1,), daemon=True).start()
    threading.Thread(target=reader, args=(2,), daemon=True).start()
    threading.Thread(target=writer, args=(1,), daemon=True).start()

    time.sleep(10)  # run for 10 seconds
