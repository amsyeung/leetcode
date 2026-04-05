"""
230. Kth Smallest Element in a BST
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""

from typing import Optional
from treeutil import TreeUtil, TreeNode

class Solution: # Time: O(N), Space: O(H)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = []
        def in_order(node):
            if not node or len(self.res) >= k:
                return
            in_order(node.left)
            if len(self.res) < k:
                self.res.append(node.val)
            if len(self.res) < k:
                in_order(node.right)
        in_order(root)
        print(self.res)
        return self.res[k - 1]

solution = Solution()
root = TreeUtil.build_tree([3,1,4,None,2])
print(solution.kthSmallest(root, 1)) # 1
root = TreeUtil.build_tree([10,1,15,None,5,None,None,4,7])
print(solution.kthSmallest(root, 3)) # 5

"""
Notes: Inorder Traversal aims to sort BST or validate BST or Expression Trees like (2 + 3) * 5
"""
