import threading
from time import sleep 

def f1():
    
    hallol = threading.Event()
    hallol.wait()
    print('hallol')
    return

def f2():
    sleep(5)
    hallol = threading.Event()
    hallol.set()
    return

t1 = threading.Thread(target=f1)
t1.start()
t2 = threading.Thread(target=f2)
t2.start()
t1.join()
t2.join()

### work with classes!!!