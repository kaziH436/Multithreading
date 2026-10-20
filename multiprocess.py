import multiprocessing
import time

square_result=[]
def cal_sq(numbers):
    global square_result
    for n in numbers:
        # time.sleep(5)
        print('square'+str(n*n))
        square_result.append(n*n)
    print('within a process result' + str(square_result))

if __name__=="__main__":
    arr=[2,3,8,9]
    p1=multiprocessing.Process(target=cal_sq, args=(arr,))
    p1.start()
    p1.join()
    print('result' + str(square_result))
    print('Done!')

# every porcess has its own address space (virtual memory). Thus program variables are not shared 
# between two processes. You need to use interprocess communication techniques if you want to share data between 
# two processes 



# def cal_sq(numbers):
#     for n in numbers:
#         time.sleep(5)
#         print('square'+str(n*n))

# def cal_cube(numbers):
#     for n in numbers:
#         time.sleep(5)
#         print('square'+str(n*n*n))

# if __name__=="__main__":
#     arr=[2,3,8,9]
#     p1=multiprocessing.Process(target=cal_sq, args=(arr,))
#     p2=multiprocessing.Process(target=cal_cube, args=(arr,))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print('Done!')