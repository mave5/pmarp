class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
from collections import deque
      
def get_number_of_islands(binaryMatrix):
  rows,cols= len(binaryMatrix),len(binaryMatrix[0])
  islands=0
  for r in range(rows):
    for c in range(cols):
      if binaryMatrix[r][c]==1:
        markIsland(binaryMatrix,rows,cols,r,c)
        islands+=1

        
  return islands

def markIsland(binaryMatrix,rows,cols,r,c):
  q=deque()
  #q = Queue()
  #q.enqueue([r,c])
  q.append([r,c])
  #while not q.isEmpty():
  while q:
    #x,y=q.dequeue()
    x,y=q.pop()
    if (binaryMatrix[x][y]==1):
      binaryMatrix[x][y]=-1
      pushIfValid(q,rows,cols,x-1,y)
      pushIfValid(q,rows,cols,x,y-1)
      pushIfValid(q,rows,cols,x+1,y)
      pushIfValid(q,rows,cols,x,y+1)
      
def pushIfValid(q,rows,cols,x,y):
  if(x>=0 and x<rows and y>=0 and y<cols):
    q.append([x,y])
  

binaryMatrix = [ [0,    1,    0,    1,    0],
                 [0,    0,    1,    1,    1],
                 [1,    0,    0,    1,    0],
                 [0,    1,    1,    0,    0],
                 [1,    0,    1,    0,    1]]


print get_number_of_islands(binaryMatrix)