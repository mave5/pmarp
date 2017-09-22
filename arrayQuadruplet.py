def find_array_quadruplet(arr,s):
  if len(arr)<4:
    return []
  
  # sorting to reduce complexity
  arr=sorted(arr)
  
  for i in range(len(arr)-4): 
    for j in range(i+1,len(arr)-3): 
      r=s-arr[i]-arr[j]
      first=j+1
      last=len(arr)-1
      
      while(first<last): 
        if (arr[first]+arr[last]>r): 
          last-=1
        elif arr[first]+arr[last]<r: 
          first+=1 
        else:
          return [arr[i],arr[j],arr[first],arr[last]]
  return []    
  
arr = [4,4,4,4]
s = 16
#arr=[2,7,4,0,9,5,1,3]
#s=20
#arr=[2,7,4,0,9,5,1,3]
#s= 120

print find_array_quadruplet(arr,s)