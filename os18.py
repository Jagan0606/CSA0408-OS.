import threading, time
from queue import Queue

buffer = Queue(maxsize=3)

def producer():
    for i in range(5):
        buffer.put(i)
        print("Produced:", i, flush=True)
        time.sleep(1)

def consumer():
    for i in range(5):
        item = buffer.get()
        print("Consumed:", item, flush=True)
        time.sleep(2)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)
t1.start()
t2.start()
t1.join()
t2.join()
