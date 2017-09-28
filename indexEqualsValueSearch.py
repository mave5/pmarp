def index_equals_value_search(arr):

  left,right=0,len(arr)-1 # 0,4
    
  while(left<=right): # true
    pivot=left+(right-left)/2 # 2 
    
    if arr[pivot]-pivot==0:#False
      return pivot # 
    elif arr[pivot]-pivot>0:
      right=pivot-1
    else:
      left=pivot+1

  return -1
  
  
  
#%%
arr =  [-8,1,4,6,7]
print index_equals_value_search(arr)