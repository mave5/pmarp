
'''
Count ways to reach the n’th stair
There are n stairs, a person standing at the bottom wants to reach the top.
 The person can climb either 1 stair or 2 stairs at a time. 
 Count the number of ways, the person can reach the top.
'''

'''
Input: n = 1
Output: 1
There is only one way to climb 1 stair

Input: n = 2
Output: 2
There are two ways: (1, 1) and (2)

Input: n = 4
Output: 5
(1, 1, 1, 1), (1, 1, 2), (2, 1, 1), (1, 2, 1), (2, 2)

'''

#%%

def countDistinctWays(n):
    numOfWays=[0]*(n+1)
    
    numOfWays[1],numOfWays[2]=1,2
        
    for i in range(3,n+1): 
        numOfWays[i]=numOfWays[i-1]+numOfWays[i-2]
    return numOfWays[n]

print countDistinctWays(5)    