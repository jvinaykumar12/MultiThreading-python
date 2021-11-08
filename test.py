import time 
import multiprocessing 
import concurrent.futures

def something(x):
    print(f'{x}f  ')
    time.sleep(x)
    print (x)
    return x
start = time.perf_counter()
with concurrent.futures.ProcessPoolExecutor(8) as pool:
    num = [3,4,2,1]
    result = [pool.submit(something,i) for i in num] 

#     # for i in concurrent.futures.as_completed(result):
#     #     print(i.result())
#     result = pool.map(something,num)
#     for ink in result:
#         print(ink)

# ps = []
# for i in range(8):
#     p = multiprocessing.Process(target = something, args=[i+1])
#     p.start()
#     ps.append(p)
end = time.perf_counter()
print(f'{round(end-start,2)}')