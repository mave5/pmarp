def array_of_array_products(arr):
  if len(arr)==0 or len(arr)==1:
    return []

  
  leftProduct=1
  rightProduct=1
  LP=[1]
  RP=[1]
  for i in range(len(arr)-1): # i=2,3
    leftProduct*=arr[i] # 2,6,24
    LP.append(leftProduct) # [1,2,6,24]

  for i in range(len(arr)-1,0,-1): # 1:1
    rightProduct*=arr[i] # 2,8,24
    RP.append(rightProduct) # RP=[2,8,24]
  RP.reverse() # [2,8,24,1]  
  #print LP,RP  
  results=[]  
  for i in range(len(arr)): # 0:4
    results.append(LP[i]*RP[i]) # 
  
  return results

arr=[1]
print array_of_array_products(arr)


def array_of_array_products(arr):
    if len(arr)==0 or len(arr)==1:
        return []
    product=1
    productArr=[1]*len(arr)
    for i in range(len(arr)):
        productArr[i]=product 
        product*=arr[i] 
  
    product=1
    for i in range(len(arr)-1,-1,-1): # 1:1
        productArr[i]*=product
        product*=arr[i] 
    return productArr
    
arr = [8, 10, 2]    
print array_of_array_products(arr)