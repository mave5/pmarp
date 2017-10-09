'''
Basic Regex Parser

Implement a regular expression function isMatch that supports the '.' and '*' symbols. The function receives two strings - text and pattern - and should return true if the text matches the pattern as a regular expression. For simplicity, assume that the actual symbols '.' and '*' do not appear in the text string and are used as special symbols only in the pattern string.

In case you aren’t familiar with regular expressions, the function determines if the text and pattern are the equal, where the '.' is treated as a single a character wildcard (see third example), and '*' is matched for a zero or more sequence of the previous letter (see fourth and fifth examples). For more information on regular expression matching, see the Regular Expression Wikipedia page.

Explain your algorithm, and analyze its time and space complexities.

Examples:

input:  text = "aa", pattern = "a"
output: false

input:  text = "aa", pattern = "aa"
output: true

input:  text = "abc", pattern = "a.c"
output: true

input:  text = "abbb", pattern = "ab*"
output: true

input:  text = "acd", pattern = "ab*c."
output: true
Constraints:

'''

#%%

def is_match(text, pattern):
  # special case
  if len(text)==0 and len(pattern)==2 and pattern[1]=='*':
    return True
 
  n=len(text)+1 # n rows
  m=len(pattern)+1 # n of cols
  
  # initialize dynamic programming table
  T=[[False]*m for i in range(n)]
  T[0][0]=True
   
  #print len(T),len(T[0])
  text=" "+text
  pattern=" "+pattern
  for i in range(1,n):
    for j in range(1,m):
      
      if text[i]==pattern[j] or pattern[j]=='.':
        T[i][j]=T[i-1][j-1]
      elif pattern[j]=='*':
        if j>=2:
          tmp=T[i][j-2]
        if text[i]==pattern[j-1] or pattern[j-1]=='.':
          tmp=tmp or T[i-1][j]
        T[i][j]=tmp
      else:
        T[i][j]=False
      #print text[i],pattern[j], T[i][j]  
  return T[n-1][m-1]
  
  

  
  
text=""
pattern="a*"
print is_match(text,pattern)  
  