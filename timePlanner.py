'''
meetingPlanner that given the availability, slotsA and slotsB,
of two people and a meeting duration dur, returns the earliest 
time slot that works for both of them and is of duration dur.
 If there is no common time slot that satisfies the duration requirement, return null.

Examples:

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]

input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: null # since there is no common slot

'''
#%%

def meeting_planner(slotsA, slotsB, dur):

  i,j=0,0
  nA=len(slotsA) # 1
  nB=len(slotsB) # 1
  while i<nA and j<nB: # i=1,j=1
  
    start = max(slotsA[i][0], slotsB[j][0]) # 7
    end = min(slotsA[i][1], slotsB[j][1]) # 11
    
    if start + dur <= end: # check starting values
      return [start, start + dur] # [60,68]
    elif slotsA[i][1] < slotsB[j][1]: 
      i+=1
    else:  
      j+=1
    
  return []  
  
  

slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8

slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 12

slotsA= [[7,12]]
slotsB= [[2,11]]
dur= 5
print meeting_planner(slotsA, slotsB, dur)  