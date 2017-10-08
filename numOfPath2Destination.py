


def num_of_paths_to_dest(n):

  memo=[[-1]*n for i in range(n)]
  
  return numOfPathsToSquare(n-1,n-1,memo)


def numOfPathsToSquare(i,j,memo):
  
  if i<0 or j<0:
    return 0
  elif i<j:
    memo[i][j]=0
  elif memo[i][j] != -1:
    return memo[i][j]
  elif i==0 and j==0:
    memo[i][j]=1
  else:
    memo[i][j]=numOfPathsToSquare(i,j-1,memo)+numOfPathsToSquare(i-1,j,memo)
  return memo[i][j]  

print num_of_paths_to_dest(10)