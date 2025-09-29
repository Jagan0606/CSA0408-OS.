import multiprocessing

def child(q):
    q.put("Hello from Child")
    print("Child sent message", flush=True)

if __name__ == "__main__":
    q = multiprocessing.Queue()

    p = multiprocessing.Process(target=child, args=(q,))
    p.start()
    p.join()

    msg = q.get()
    print("Parent received:", msg, flush=True)

