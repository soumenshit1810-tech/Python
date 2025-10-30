import threading
import time

def display(msg):
    for i in range(3):
        time.sleep(1)
        print(msg)

t1 = threading.Thread(target=display, args=("Thread 1 running",))
t2 = threading.Thread(target=display, args=("Thread 2 running",))

t1.start()
t2.start()

t1.join()
t2.join()

print("All threads finished!")
