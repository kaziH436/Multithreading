import multiprocessing
import time


def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire() # this is critical section
        balance.value=balance.value+1
        lock.release()

def withdraw (balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value=balance.value-1
        lock.release()

if __name__=="__main__":
    balance = multiprocessing.Value('i',200)
    lock=multiprocessing.Lock()
    d=multiprocessing.Process(target=deposit, args=(balance, ))
    w=multiprocessing.Process(target=withdraw, args=(balance,))

    d.start()
    w.star()

    d.join()
    w.join()
    w.join()
    print('Done!')

# Why is lock needed? Resources can't be assesed at the same time 

# In process and threads, there are shared resources to protect using locks 