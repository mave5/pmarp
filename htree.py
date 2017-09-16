
# H-Tree Construction# 

import math


def drawLine(x1,y1,x2,y2):
  print(x1,y1,x2,y2)


def drawHTree(x,y,length,depth):
  #drawHTree.counter+=1
  #print(drawHTree.counter)
  if depth==0:
    return

  # coordinates
  x0=x-length/2
  x1=x+length/2
  y0=y-length/2
  y1=y+length/2
  
  # draw center
  drawLine(x0,y,x1,y)
  # draw left
  drawLine(x0,y0,x0,y1)
  # draw center
  drawLine(x1,y0,x1,y1)

  drawHTree(x0,y0,length/math.sqrt(2),depth-1)
  drawHTree(x0,y1,length/math.sqrt(2),depth-1)    
  drawHTree(x1,y0,length/math.sqrt(2),depth-1)    
  drawHTree(x1,y1,length/math.sqrt(2),depth-1)    

#%%    
drawHTree(1000,1000,100,2)  