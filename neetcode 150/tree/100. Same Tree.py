"""
100. Same Tree
Easy
Topics
premium lock icon
Companies
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
"""

from typing import Optional
from TreeUtil import TreeNode, TreeUtil

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

solution = Solution()
print(solution.isSameTree(TreeUtil.build_tree([1, 2, 3]), TreeUtil.build_tree([1, 2, 3]))) # True
print(solution.isSameTree(TreeUtil.build_tree([1, 2]), TreeUtil.build_tree([1, None, 2]))) # False
print(solution.isSameTree(TreeUtil.build_tree([1, 2, 1]), TreeUtil.build_tree([1, 1, 2]))) # False

"""
Time Complexity: O(N), O(min(P, Q))
Space Complexity: O(H)
"""