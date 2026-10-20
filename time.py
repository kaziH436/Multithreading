import time
import threading 

def cal_sq(numbers):
    print('Calclate sqaures')
    for n in numbers:
        time.sleep(0.2) # CPU idle 
        print('square', n*n)

def cal_cube(numbers):
    print('calculate cubes')
    for n in numbers:
        time.sleep(0.2)
        print('cube', n*n*n)

arr=[2,3,4,5]
t=time.time()
# cal_sq(arr)
# cal_cube(arr)
t1 = threading.Thread(target=)