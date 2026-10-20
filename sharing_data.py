import multiprocessing
import time

# shared memory using array 
square_result=[]
def cal_sq(numbers, result):
    #global square_result # multiprocesses create a copy 
    for idx, n in enumerate(numbers):
        # time.sleep(5)
        #print('square'+str(n*n))
        #square_result.append(n*n)
        result[idx]=n*n
    #print('within a process result' + str(square_result)) # this updates the copy not the actual global variable 
# to solve, use shared memory
 
if __name__=="__main__":
    arr=[2,3,8,9]
    result=multiprocessing.Array('i',3)
    p1=multiprocessing.Process(target=cal_sq, args=(arr,result))
    p1.start()
    p1.join()
    print(result[:]) 





# shared memory using Value 
square_result=[]
def cal_sq(numbers, result):
    v.value=6.7
    for idx, n in enumerate(numbers):
        # time.sleep(5)
        #print('square'+str(n*n))
        #square_result.append(n*n)
        result[idx]=n*n
    #print('within a process result' + str(square_result)) # this updates the copy not the actual global variable 
# to solve, use shared memory
 
if __name__=="__main__":
    arr=[2,3,8,9]
    result=multiprocessing.Array('i',3)
    v=multiprocessing.Value('d',0.0)
    p1=multiprocessing.Process(target=cal_sq, args=(arr,v))
    p1.start()
    p1.join()
    print(result[:]) 