"""
226. Invert Binary Tree
Easy
Topics
premium lock icon
Companies
Given the root of a binary tree, invert the tree, and return its root.

 

Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []
"""

from typing import Optional
from TreeUtil import TreeNode, TreeUtil

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

l = [4, 2, 7, 1, 3, 6, 9]
root = TreeUtil.build_tree(l)

solution = Solution()
TreeUtil.print_tree(solution.invertTree(root))

"""
Time Complexity: O(n), visit every node, where n is the number of Nodes
Space Complexity: O(H), recursive loop used -> depends on call stack -> depends on height on the Tree
"""
