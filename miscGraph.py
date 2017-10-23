
## misc graph
#%%

'''
In this problem, a rooted tree is a directed graph such that, there is exactly 
one node (the root) for which all other nodes are descendants of this node, 
plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes
 (with distinct values 1, 2, ..., N), with one additional directed edge added.
 The added edge has two different vertices chosen from 1 to N, and was not an
 edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges 
is a pair [u, v] that represents a directed edge connecting nodes u and v, 
where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted
 tree of N nodes. If there are multiple answers, return the answer that 
 occurs last in the given 2D-array.

Example 1:

Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3

Example 2:

Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3

'''

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        visited=[]
        for (u,v) in edges:
            if u in visited and v in visited:
                candidate=[u,v]
            if u not in visited:
                visited.append(u)
            if v not in visited:
                visited.append(v)
        return candidate        
#edges=[[1,2],[1,3],[2,3]]              
#edges=[[3,4],[1,2],[2,4],[3,5],[2,5]]
edges=[[9,10],[5,8],[2,6],[1,5],[3,8],[4,9],[8,10],[4,10],[6,8],[7,9]]
sol=Solution()  
print sol.findRedundantConnection(edges)
[6,8]


#%%

'''

Given a list of airline tickets represented by pairs of departure and arrival
airports [from, to], reconstruct the itinerary in order. All of the tickets 
belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

    If there are multiple valid itineraries, you should return the itinerary
    that has the smallest lexical order when read as a single string. 
    For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    All airports are represented by three capital letters (IATA code).
    You may assume all tickets form at least one valid itinerary.

Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].

loop over tickets, find JFK first, 

Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. 
But it is larger in lexical order. 

    
'''

#%%