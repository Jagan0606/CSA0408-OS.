# thread_basics.py
# Demonstrates create, join, equality (comparing thread identities), and exit
import threading
import time
import sys

def worker(name):
    print(f"Worker {name} started (thread id: {threading.get_ident()})")
    time.sleep(0.5)
    print(f"Worker {name} finishing")
    # return from function == thread exit

if __name__ == "__main__":
    # create
    t1 = threading.Thread(target=worker, args=("A",), name="T-A")
    t2 = threading.Thread(target=worker, args=("B",), name="T-B")

    t1.start()
    t2.start()

    # equality: compare thread objects or id
    print("t1 == t2 ?", t1 == t2)
    print("t1.name, t2.name:", t1.name, t2.name)
    print("t1.ident, t2.ident:", t1.ident, t2.ident)

    # join: wait for threads to finish
    t1.join()
    t2.join()
    print("Both threads joined. Exiting main thread.")
    sys.exit(0)
