
#Bracket Match

# A string of brackets is considered correctly matched if every opening bracket 
# in the string can be paired up with a later closing bracket, and vice versa. 
# For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. 
# For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.
def bracket_match(text):
  if len(text)==0:
    return 0
  
  
  counter=0
  counter2=0
  for t in text: # (,),)
    if t=='(':
      counter2+=1
    elif (counter2>0) and (t==')'):
      counter2-=1
    else: #if(len(stack1)==0) and (t==')'):
      counter+=1 # counter=1
  
  
        
  return counter+counter2
  
      