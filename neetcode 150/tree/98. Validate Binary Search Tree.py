"""
98. Validate Binary Search Tree
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys strictly less than the node's key.
The right subtree of a node contains only nodes with keys strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

from typing import Optional
from treeutil import TreeUtil, TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, left_bound, right_bound):
            if not node:
                return True
            if not(left_bound < node.val < right_bound):
                return False
            return dfs(node.left, left_bound, node.val) and \
                    dfs(node.right, node.val, right_bound)
        return dfs(root, float('-inf'), float('inf'))

solution = Solution()
root = TreeUtil.build_tree([2,1,3])
print(solution.isValidBST(root)) # True
root = TreeUtil.build_tree([5,1,4,None,None,3,6])
print(solution.isValidBST(root)) # False

"""
Time Complexity: O(n)
Space Complexity: O(H)
"""
