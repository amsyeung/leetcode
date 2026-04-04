"""
110. Balanced Binary Tree
Easy
Topics
premium lock icon
Companies
Given a binary tree, determine if it is height-balanced.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
"""

from typing import Optional
from treeutil import TreeNode, TreeUtil

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(node):
            if not node:
                return 0
            
            l = getHeight(node.left)
            if l == -1:
                return -1
            
            r = getHeight(node.right)
            if r == -1: 
                return -1
            
            if abs(r - l) > 1: 
                return -1
            
            return 1 + max(l, r)
        return getHeight(root) != -1

l = [3,9,20,None,None,15,7]
root = TreeUtil.build_tree(l)
solution = Solution()
print(solution.isBalanced(root)) # True

"""
Time Complexity: O(n)
Space Complexity: O(h), the worse case is skewed binary tree
"""
