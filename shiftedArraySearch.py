
def shifted_arr_search(shiftArr, num):
  
  # find pivot: number of shifts
  pivot=findPivotPoint(shiftArr)
  
  if pivot==0 or num<shiftArr[0]:
    return bsearch(shiftArr,pivot,len(shiftArr)-1,num)
  
  return bsearch(shiftArr,0,pivot-1,num)


def bsearch(arr,left,right,num):
  while left<=right:
    p=(left+right)//2
    if arr[p]==num:
      return p
    elif arr[p]>num:
      right=p-1
    else:
      left=p+1
  return -1   

def findPivotPoint(arr):
  
  left,right=0,len(arr)-1 # 0,5
  
  while left<=right:
    p=left+(right-left)/2 # p=5
    if arr[p-1]>arr[p] or p==0:  
      return p
    elif arr[p]>arr[0]: 
      left=p+1 # left=5
    else: # arr[p]<arr[0]
      right=p-1
  return 0      
    
  
shiftArr = [1,2,3,4,5,0]
num= 0
print shifted_arr_search(shiftArr,num)

