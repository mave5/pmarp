

def find_grants_cap(grantsArray, newBudget):
  
  n=len(grantsArray)
  # sort the array
  grantsArray.sort(reverse=True)
  
  # pad with zero
  grantsArray.append(0)
  
  # calculate budget difference
  surplus=sum(grantsArray)-newBudget
  
  # nothing to cut
  if surplus<=0:
    return grantsArray[0]
  
  for i in range(n):
    surplus-=(i+1)*(grantsArray[i]-grantsArray[i+1])
    if surplus<=0:
      break
  return grantsArray[i+1]+(-surplus/float(i+1))

#%%
grantsArray = [2, 100, 50, 120, 1000]
newBudget = 190

print find_grants_cap(grantsArray,newBudget)