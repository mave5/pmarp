

#%% fibonachi using memoization

def fib(n,cache={}):
    if n<=1:
        return 1
    elif n not in cache:
        cache[n]=fib(n-1)+fib(n-2)
    return cache[n]

import time
start=time.time()
print fib(30)
print ('elapsed time:' ,(time.time()-start)*1000)
#%%
# fib using only recursion

def fib(n):
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

start=time.time()
print fib(30)
print ('elapsed time:' ,(time.time()-start)*1000)
