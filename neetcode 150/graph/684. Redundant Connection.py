"""
684. Redundant Connection
Medium
Topics
premium lock icon
Companies
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
"""

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x]) # path compression, flat the tree
            return parent[x]
        for u, v in edges:
            pu, pv = find(u), find(v)
            if pu == pv:
                return [u, v]   
            parent[pu] = pv     
    
solution = Solution()
print(solution.findRedundantConnection([[1,2],[1,3],[2,3]])) # [2,3]

"""
Time: O(n * α(n)) ≈ O(n), where n = len(edges); each edge does find/union
Space: O(n) — parent array
"""