f"""
(Premium)
Number of Connected Components in an Undirected Graph
Medium
Topics
Company Tags
Hints
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.

Return the number of connected components in the graph.

Example 1:



Input:
n = 5, edges = [[0,1],[1,2],[3,4]]

Output: 2
Example 2:



Input:
n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]

Output: 1
Constraints:

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= aᵢ <= bᵢ < n
aᵢ != bᵢ
There are no repeated edges.
"""

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()
        count = 0
        def dfs(node):
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count
    
solution = Solution()
print(solution.countComponents(5, [[0,1],[1,2],[3,4]])) # 2

"""
Time: O(n + m)
Space: O(n + m)
"""