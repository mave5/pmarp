

def transpose_and_yield_top(inputMatrix):
  result=[]
  while inputMatrix:
    result.append(inputMatrix[0])
    inputMatrix= list(reversed(zip(*inputMatrix[1:])))
  return result  

def spiral_copy(inputMatrix):
  return list(itertools.chain(*transpose_and_yield_top(inputMatrix)))



inputMatrix  = [ [1,    2,   3,  4,    5],
                 [6,    7,   8,  9,   10],
                 [11,  12,  13,  14,  15],
                 [16,  17,  18,  19,  20] ]

print spiral_copy(inputMatrix)


#%% using generator
import itertools

# generator
def transpose_and_yield_top(inputMatrix):
  while inputMatrix:
    yield inputMatrix[0]
    inputMatrix= list(reversed(zip(*inputMatrix[1:])))


def spiral_copy(inputMatrix):
  return list(itertools.chain(*transpose_and_yield_top(inputMatrix)))


inputMatrix  = [ [1,    2,   3,  4,    5],
                 [6,    7,   8,  9,   10],
                 [11,  12,  13,  14,  15],
                 [16,  17,  18,  19,  20] ]

print spiral_copy(inputMatrix)