"""
Graph Valid Tree
Medium
Topics
Company Tags
Hints
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:

Input:
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

Output:
true
Example 2:

Input:
n = 5
edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]

Output:
false
Note:

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1) / 2
"""

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()
        def hasCycle(node, parent):
            visited.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return True
                if hasCycle(nei, node):
                    return True
            return False
        if hasCycle(0, -1):
            return False
        return len(visited) == n
        

solution = Solution()
print(solution.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])) # True
print(solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])) # False

"""
Time: O(n + m), where n is number of nodes and m is number of edges.
Space: O(n + m) for adjacency list, visited set, and recursion stack.
    For a valid tree m = n - 1, so both can be viewed as O(n).
"""
