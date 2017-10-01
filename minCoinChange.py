'''
Find minimum number of coins that make a given value
Given a value V, if we want to make change for V cents, 
and we have infinite supply of each of C = { C1, C2, ..,Cm} valued coins,
what is the minimum number of coins to make the change?

Examples:
'''
#%%


def coinChange(coins, amount):
    MAX = float('inf')
    dp = [0] + [MAX] * amount
    
    for i in xrange(1, amount + 1):
        dp[i] = min([dp[i - c] if i - c >= 0 else MAX for c in coins]) + 1
     
    return [dp[amount], -1][dp[amount] == MAX]    
    

    
    
#%%

def coinChange2(coins,amount):
    MAX=float('inf')
    
    # initialize memory
    dp=[0]+ [MAX]*amount # len(dp)=amount+1, dp=[0,inf,inf,....]
    
    for a in xrange(1,amount+1):
        tmpdp=[]
        for c in coins:
            if a-c>=0:
                tmp=dp[a-c]
            else:
                tmp=MAX
            tmpdp.append(tmp)    
        dp[a]=min(tmpdp)+1
          
    if dp[amount]==MAX:
        return -1
    else:
        return dp[amount]
        
        
coins=[1,2,3] 
amount=5  
print coinChange2(coins,amount)    


coins=[1,2,3] 
amount=5  
print coinChange(coins,amount)    
        