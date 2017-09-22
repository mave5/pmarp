def checkArrInSubstring(arr,subS):
    for c in arr:
        if c not in subS:
            return False
    return True        
    
def get_shortest_unique_substring(arr, S):
    if len(arr)>len(S):
      return ""
    
    start=0
    end=len(arr)
    result=S
    while(end<=len(S)):
        if not checkArrInSubstring(arr,S[start:end]):
            end+=1
        else:
            while checkArrInSubstring(arr,S[start+1:end]):
                start+=1
               
            if len(S[start:end])<=len(result):
                result=S[start:end]
                if len(result)==len(arr):
                  return result
            start=end
            end=start+len(arr)
            
 
    return result


#arr = ['x','y','z']
#S = "xyyzyzyx"  
arr=["A","B","C"] 
S="ADOBECODEBANCDDD"
print get_shortest_unique_substring(arr,S)                      