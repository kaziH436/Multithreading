import time
import threading 

def cal_sq(numbers):
    print('Calclate sqaures')
    for n in numbers:
        time.sleep(0.2) # CPU idle: when the cpu is idle for this, the other function will be excuting  
        print('square', n*n)

def cal_cube(numbers):
    print('calculate cubes')
    for n in numbers:
        time.sleep(0.2)
        print('cube', n*n*n)

arr=[2,3,4,5]
t=time.time() # time needs to be placed here 
# cal_sq(arr)
# cal_cube(arr)
t1 = threading.Thread(target=cal_sq, args=(arr,))
t2 = threading.Thread(target=cal_cube, args=(arr,))

t1.start() # execute programs in parallel
t2.start()

t1.join() # wait till t1 is finished 
t2.join()

print('done in: ', time.time()-t)
# Calclate sqaures 
# calculate cubes
# square 4
# cube 8
# cube 27
# square 9
# cube 64
# square 16
# cube 125
# square 25