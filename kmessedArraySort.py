

import heapq      

def sort_k_messed_array(arr, k):
 
  n=len(arr) 
  h = [] 
    
  for i in range(0,k+1):  
      heapq.heappush(h,arr[i]) 
  
  for i in range(k+1,n): 
      arr[i-(k+1)]=heapq.heappop(h)
      heapq.heappush(h,arr[i])
          
  for i in range(k+1):  
      arr[n-(k+1)+i]=heapq.heappop(h) #2-0+1
    
  return arr    


arr=[1,0]
k=1
print sort_k_messed_array(arr,k)