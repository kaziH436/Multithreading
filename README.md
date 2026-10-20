# Multithreading
pre-req for c++ trading systems

codebasics [Python Tutorial - 26. Multithreading - Introduction](https://www.youtube.com/watch?v=PJ4t2U15ACo&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN)

## Difference between Multithreading and multiprocessing 
multiprocessing: all programs running on a laptop are different processes
- The multiprocess can communicate by using file on disk, shared memory, message pipeline
- The benefit of multiprocessing is that error or memory leak in one process won't hurt execution of another process 


multithreading: within a process, there can be multible threads
Each thread will do its wn tasks (heap memory can be accessed) 
    - lightweight and memory leak can affect the other threads



