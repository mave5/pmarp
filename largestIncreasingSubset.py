
#%%
import random

def largestIncreasingSubset(A):
    n=len(A)
    dp=[1]*n
    for i in range(1,n):
        for j in range(0,i):
            if A[i]>A[j] and dp[i]<dp[j]+1:
                dp[i]=dp[j]+1
    
    maxLis=0
    for i in range(n):
        maxLis=max(maxLis,dp[i])        
    return maxLis


#%%
n=5

A=[random.randint(0,100) for i in range(n)]
print 'array:', A
print 'largest length of increasing subset:', largestIncreasingSubset(A)
