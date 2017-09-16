
# Merging 2 Packages

def get_indices_of_item_wights(arr, limit):
  if len(arr)==1:
    return []
  #elif (len(arr)==2) and (arr[0]+arr[1]==limit):
    #print arr[0],arr[1],arr[0]+arr[1]
    #return []
  comps={}
  for i in range(0,len(arr)):
    w=arr[i]
    j=comps.get(lim-w)
    if j is not None:
      return [j,i]
    else:
      comps[w]=i
  return []

arr = [4, 4]  
lim = 8

print get_indices_of_item_wights(arr,lim)