"""
104. Maximum Depth of Binary Tree
Solved
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
"""

from typing import Optional
from TreeUtil import TreeUtil, TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]):
        if not root:
            return 0
        l = 1 + self.maxDepth(root.left)
        r = 1 + self.maxDepth(root.right)
        max_depth = max(l, r)
        return max_depth

l = [3, 9, 20, None, None, 15, 7]
root = TreeUtil.build_tree(l)
TreeUtil.print_tree(root)

solution = Solution()
print(solution.maxDepth(root))

"""
Time Complexity: O(n), where n is numbers of nodes traveled
Space Complexity: O(h), where h is height of the Tree
"""