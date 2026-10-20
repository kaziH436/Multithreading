from multiprocessing import Pool
import time 

def f(n):
    sum=0
    for x in range(1000):
        sum+=x*x
    return sum

if __name__ == "__main__":
    t1=time.time() # current time 
    p=Pool()
    result=p.map(f,range(100000))
    p.close()
    p.join()
    print("Pool took ", time.time()-t1)

    t2=time.time()
    result=[]
    for x in range(100000):
        result.append(f(x))
    print("serial processing took ", time.time()-t2)

# Parallel Processing 
# map: dividing the input into multiple cores in the CPU equally 
# reduce: aggregate the results back into the output
