import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(5):
        with lock:
            counter += 1
            print("Counter:", counter, flush=True)

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final Counter:", counter, flush=True)
