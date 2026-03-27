"""
572. Subtree of Another Tree
Easy
Topics
premium lock icon
Companies
Hint
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

 

Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false
"""

from typing import Optional
from treeutil import TreeUtil, TreeNode

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def isSame(s, t):
            if not s and not t:
                return True
            if not s or not t or s.val != t.val:
                return False
            return isSame(s.left, t.left) and isSame(s.right, t.right)
        return isSame(root, subRoot) or \
                self.isSubtree(root.left, subRoot) or \
                    self.isSubtree(root.right, subRoot)

solution = Solution()
print(solution.isSubtree(TreeUtil.build_tree([3,4,5,1,2]), TreeUtil.build_tree([4,1,2]))) # True
print(solution.isSubtree(TreeUtil.build_tree([3,7,None,9,None,None,10,11,12]), TreeUtil.build_tree([10, 11, 12]))) # True
print(solution.isSubtree(TreeUtil.build_tree([3,4,5,1,2,None,None,None,None,0]), TreeUtil.build_tree([4,1,2]))) # False

"""
Time Complexity: O(M * N), M is the number of nodes in the main tree while N is the number of nodes in the subtree
Space Complexity: O(H), H is the height of the main tree. The worst case happened when the tree is skewed.
"""
