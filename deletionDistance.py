def deletion_distance(str1, str2):
  #if len(str1)==0 or len(str2)==0:
    #return max(len(str1),len(str2))

  if len(str1)<len(str2):
    str1,str2=str2,str1
    
  index=0
  match=0
  for c2 in str2: 
    for i1,c1 in enumerate(str1): 
      if c1==c2 and i1>=index: 
        index=i1 
        match+=1
        break
    
  return len(str1)+len(str2) - 2*match 

def deletion_distance_dp(str1, str2):
  if len(str1) > len(str2):
    str1, str2 = str2, str1
  prev = range(len(str1) + 1)
  
  for i in range(1, len(str2)+1):
    curr = [0 for _ in range(len(str1) + 1)]
    for j in range(len(str1)+1):
      if j == 0:
        curr[j] = i
      else:
        if str1[j-1] == str2[i-1]:
          curr[j] = prev[j-1]
        else:
          curr[j] = min(curr[j-1], prev[j]) + 1
    prev = curr
  return prev[-1]

str1 = "e"
str2 = "aaaezzzzze"
  
  
print deletion_distance(str1, str2)
print deletion_distance_dp(str1, str2)