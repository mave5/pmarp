

# Pairs with Specific Difference

def find_pairs_with_given_difference(arr, k):
  
  arr=sorted(arr)
 
  answer=[]
  first=0
  last=1
  
  while (last<len(arr)) and (first<len(arr)):
    
    if (first!=last) and (arr[last]-arr[first]==k):
      answer.append([arr[last],arr[first]])
      first+=1
      last+=1
    elif(arr[last]-arr[first]<k):
      last+=1
    else:
      first+=1
        
  return answer

 
arr = [1,5,11,7]
k=6

print find_pairs_with_given_difference(arr,k)



