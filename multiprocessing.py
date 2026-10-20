import multiprocessing


def cal_sq(numbers):
    for n in numbers:
        time.sleep(5)
        print('square'+str(n*n))

if __name__=="__main__":
    arr=[2,3,8,9]
    p1=multiprocessing.Process(target=cal_sq, args=(arr,))

    p1.start()

    p1.join()
    print('result' + )
    print('Done!')




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