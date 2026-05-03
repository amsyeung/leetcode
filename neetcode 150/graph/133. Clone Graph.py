"""
133. Clone Graph
Medium
Topics
premium lock icon
Companies
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

 

Example 1:


Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: There are 4 nodes in the graph.
1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
Example 2:


Input: adjList = [[]]
Output: [[]]
Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.
Example 3:

Input: adjList = []
Output: []
Explanation: This an empty graph, it does not have any nodes.
"""

from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None

        old_to_new: dict[Node, Node] = {}

        def clone(n: Node) -> Node:
            if n in old_to_new:
                return old_to_new[n]
            copy = Node(n.val)
            old_to_new[n] = copy
            for nei in n.neighbors:
                copy.neighbors.append(clone(nei))
            return copy

        return clone(node)


solution = Solution()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors.extend([node2, node4])
node2.neighbors.extend([node1, node3])
node3.neighbors.extend([node2, node4])
node4.neighbors.extend([node1, node3])
solution.cloneGraph(node1) # [[2,4],[1,3],[2,4],[1,3]]

"""
Complexity (V = nodes, E = edges, DFS + old_to_new map):

Time: O(V + E)
  Each original node is cloned at most once (first visit); later visits are O(1) map lookup.
  Summing |neighbors| over all nodes is the degree sum; in an undirected graph that is 2E,
  so scanning all adjacency lists is O(E). Total O(V + E).

Space: O(V) auxiliary
  old_to_new holds at most one entry per original node.
  DFS call stack depth is O(V) in the worst case (e.g. a long path).
  The returned clone itself stores O(V) nodes and O(E) neighbor references — often stated
  separately as O(V + E) output space, not extra beyond the answer.
"""