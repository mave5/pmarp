'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

solution: sort then check for overlaps in linear complexity
[a b] [c d]
if a>c and b<d then [a b] is inside [c d]
if a>c and b>d then merge=[c b]
'''
#%%
'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note that if you end up using an additional array, you will only receive partial score.

Example:

If the array is

[
    [1, 2],
    [3, 4]
]
Then the rotated array becomes:

[
    [3, 1],
    [4, 2]
]

solution: swap row [i] with column [n-1-i]
or element [i][j] -> [j][n-1-i]
'''
#%%

'''
Given an index k, return the kth row of the Pascal’s triangle.

Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.

Example:

Input : k = 3

Return : [1,3,3,1]
NOTE : k is 0 based. k = 0, corresponds to the row [1]. 
Note:Could you optimize your algorithm to use only O(k) extra space?

solution: recursive function (like fibonachi) or using memoisation
base case k=0 => [1]
k=1 => [1,1]
k>1 => init [1], for i in range(k-1), append pascal[k-1][i]+pascal[k-1][i+1], append [1]
'''
#%%

'''

There are two sorted arrays A and B of size m and n respectively.
Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ).
The overall run time complexity should be O(log (m+n)).

A : [1 4 5]
B : [2 3]
[1 2 3 4 5] => 3
[1 4 5 2 3]
- simple solution: merge two arrays and then find median: O(n+m)
- different cases
 
'''

#%%

'''
Given a sorted array of integers, find the starting and ending position of 
a given target value.

Your algorithm’s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example:

Given [5, 7, 7, 8, 8, 10]
[5, 7, 7, 8, 8, 9,10,11,12]

and target value 8,

return [3, 4].

- brute force: for loop: O(N)
- BS to find first item
- BS to find the last item

'''
#%%

'''
Implement pow(x, n) % d.

In other words, given x, n and d,

find (x**n % d)

Note that remainders on division cannot be negative. 
In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.

(a %d) (b%d)= ab %d
((a%d)(b%d)) %d=ab%d


'''
#%%

'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7  might become 4 5 6 7 0 1 2 ).

You are given a target value to search. If found in the array, return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Input : [4 5 6 7 0 1 2] and target = 4
Output : 0


find the pivot point using BS, then divide into two sub-arrays and use BS to find target
- to find pivot point using BS: find the point that A[pivot]>A[pivoit-1]
'''
#%%

'''

N number of books are given. 
The ith book has Pi number of pages. 
You have to allocate books to M number of students so that maximum 
number of pages alloted to a student is minimum. A book will be allocated
to exactly one student. Each student has to be allocated at least one book. 
Allotment should be in contiguous order, for example: A student cannot be
allocated book 1 and book 3, skipping book 2.

NOTE: Return -1 if a valid assignment is not possible

Input:

List of Books
M number of students
Your function should return an integer corresponding to the minimum number.

Example:

P : [12, 34, 67, 90]
M : 2

Output : 113

There are 2 number of students. Books can be distributed in following fashion : 
  1) [12] and [34, 67, 90]
      Max number of pages is allocated to student 2 with 34 + 67 + 90 = 191 pages
  2) [12, 34] and [67, 90]
      Max number of pages is allocated to student 2 with 67 + 90 = 157 pages 
  3) [12, 34, 67] and [90]
      Max number of pages is allocated to student 1 with 12 + 34 + 67 = 113 pages

Of the 3 cases, Option 3 has the minimum pages = 113. 


''''

'''
- if N<M then not possible
- if N=M then find the book with max pagaes
- if N>M:
 

'''
#%%


'''
Painter's Partition Problem
You have to paint N boards of length {A0, A1, A2, A3 … AN-1}. 
There are K painters available and you are also given how much time a painter 
takes to paint 1 unit of board. You have to get this job done as soon
as possible under the constraints that any painter will only
 paint contiguous sections of board.

2 painters cannot share a board to paint. That is to say, a board
cannot be painted partially by one painter, and partially by another.
A painter will only paint contiguous boards. Which means a
configuration where painter 1 paints board 1 and 3 but not 2 is
invalid.
Return the ans % 10000003

Input :
K : Number of painters
T : Time taken by painter to paint 1 unit of board
L : A List which will represent length of each board

Output:
     return minimum time to paint all boards % 10000003
Example

Input : 
  K : 2
  T : 5
  L : [1, 10]
Output : 50

Given an array of non-negative integers A and a positive integer k, we want to:
Divide A into k or fewer partitions,
such that the maximum sum over all the partitions is minimized.

'''

#%%

'''
Write a function to find the longest common prefix string amongst an array of strings.

Longest common prefix for a pair of strings S1 and S2 is the longest string S 
which is the prefix of both S1 and S2.

As an example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".

Given the array of strings, you need to find the longest S which is
 the prefix of ALL the strings in the array.

Example:

Given the array as:

[

  "abcdefgh",

  "aefghijk",

  "abcefgh"
]
The answer would be “a”.

brute force:
- find shortest string O(N)
- loop over shortest string: SS O(M)
- check if each char of SS in all strings: O(N) => O(NM)

better solution
- find shortest string: SS =>O(N)
- use BS: divide SS into two sub-strings O(NM log M)
- check if left sub is in all
- then check of right sub in all

#%%

Given two numbers represented as strings, return multiplication of the numbers as a string.

Note: The numbers can be arbitrarily large and are non-negative.
Note2: Your answer should not have leading zeroes. For example, 00 is not a valid answer. 
For example, 
given strings "12", "10", your answer should be “120”.

12,11
- basic math
- 1*2=2,0
-1*1+0=1,0
- 2+1*10=12

 
 #%%

Justified Text
Given an array of words and a length L, format the text such that each 
line has exactly L characters and is fully (left and right) justified.
You should pack your words in a greedy approach; 
that is, pack as many words as you can in each line.

Pad extra spaces ‘ ‘ when necessary so that each line has exactly L characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and
no extra space is inserted between words.

Your program should return a list of strings, 
where each string represents a single line.

Example:

words: ["This", "is", "an", "example", "of", "text", "justification."]

L: 16.

Return the formatted lines as:

[
   "This    is    an",
   "example  of text",
   "justification.  "
]

- set a counter for the number of spaces in each line
- set a counter for the number of chr in each line
- for each word we check if len(word)+1+counter<=L, one is added for space
- if yes, we append the word and increase counter and numOfWords
- if not, we calculate L-counter and divide it to the number of spaces

#%%
Find the element that appears once
4.2
Given an array where every element occurs three times, 
except one element which occurs only once. Find the element that
occurs once. Expected time complexity is O(n) and O(1) extra space.
Examples:

Input: arr[] = {12, 1, 12, 3, 12, 1, 1, 2, 3, 3}
Output: 2


def special(lst):
    ones = 0
    twos = 0
    for x in lst: # 12
        twos |= ones & x # 0
        #print twos
        ones ^= x # 1
        not_threes = ~(ones & twos) # 0
        ones &= not_threes # 0
        twos &= not_threes #0
        print ones
    return ones

A=[12, 1, 12, 3, 12, 1, 1, 2, 3, 3]
print special(A)
'''

#%%

Find the intersection of two sorted arrays.
OR in other words,
Given 2 sorted arrays, find all the elements which occur in both the arrays.

Example :

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 3 5]

Output : [3 3 5]

Input : 
    A : [1 2 3 3 4 5 6]
    B : [3 5]

Output : [3 5]


two pointers
For Intersection of two arrays, print the element only if the element is present in both arrays.
1) Use two index variables i and j, initial values i = 0, j = 0
2) If arr1[i] is smaller than arr2[j] then increment i.
3) If arr1[i] is greater than arr2[j] then increment j.
4) If both are same then print any of them and increment both i and j.
    
#%%

Remove Duplicates from Sorted Array
Remove duplicates from Sorted Array
Given a sorted array, remove the duplicates in place such that each element appears only once and return the new length.

Note that even though we want you to return the new length, make sure to change the original array as well in place

Do not allocate extra space for another array, you must do this in place with constant memory.

Example: 
Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2]. 

solution: two pointers

#%%
   
Find three closest elements from given three sorted arrays
3.5
Given three sorted arrays A[], B[] and C[], find 3 elements i, j and k from A, B and C respectively such that max(abs(A[i] – B[j]), abs(B[j] – C[k]), abs(C[k] – A[i])) is minimized. Here abs() indicates absolute value.

Example :

Input: A[] = {1, 4, 10}
       B[] = {2, 15, 20}
       C[] = {10, 12}
Output: 10 15 10
10 from A, 15 from B and 10 from C

Input: A[] = {20, 24, 100}
       B[] = {2, 19, 22, 79, 800}
       C[] = {10, 12, 23, 24, 119}
Output: 24 22 23
24 from A, 22 from B and 23 from C

solution: three pointers
find max(A[i],B[j],C[k]) and min(A[i],B[j],C[k])
diff=max-min
update diff if it is less than previous
increase index of min
#%%

Container With Most Water
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
'n' vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Your program should return an integer which corresponds to the maximum area of water that can be contained ( Yes, we know maximum area instead of maximum volume sounds weird. But this is 2D plane we are working with for simplicity ).

Note: You may not slant the container. 
Example :

Input : [1, 5, 4, 3]
Output : 6

Explanation : 5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3. 
So total area = 3 * 2 = 6


solution: two pointers starting at i=0,j=end
find maxArea
move shorter line to right/left and compare

#%% 

'''
Sort List
Sort a linked list in O(n log n) time using constant space complexity.

Example :

Input : 1 -> 5 -> 4 -> 3

Returned list : 1 -> 3 -> 4 -> 5

merge sort
'''
#%%

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
  
solution: use a stack to push numbers, once see an operator pop
push 2,1 => 1+2=> push 3,3 * => push 9
push 4,13,5 => pop 5,13 => push 13/5 => pop 13/5 and 4 => 4+13/5

#%%
Largest Rectangular Area in a Histogram | Set 2
4.2
Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have same width and the width is 1 unit.

For example, consider the following histogram with 7 bars of heights {6, 2, 5, 4, 5, 1, 6}. The largest possible rectangle possible is 12 (see the below figure, the max area rectangle is highlighted in red)
 
solution: stack
  
 #%% 

