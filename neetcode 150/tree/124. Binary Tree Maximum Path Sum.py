"""
124. Binary Tree Maximum Path Sum
Hard
Topics
premium lock icon
Companies
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
"""

from typing import Optional
from treeutil import TreeNode, TreeUtil

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')
        def dfs(node):
            if not node:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return self.max_sum
        
solution = Solution()
root = TreeUtil.build_tree([1,2,3])
print(solution.maxPathSum(root)) # 6
root = TreeUtil.build_tree([-10,9,20,None,None,15,7])
print(solution.maxPathSum(root)) # 42

"""
Time Complexity: O(n), each node is visited exactly once
Space Complexity: O(h) for recursion stack, where h is tree height (balanced: O(log n), worst-case skewed: O(n))
"""