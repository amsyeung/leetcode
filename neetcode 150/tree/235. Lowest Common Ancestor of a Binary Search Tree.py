"""
235. Lowest Common Ancestor of a Binary Search Tree
Medium
Topics
premium lock icon
Companies
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""

from treeutil import TreeNode, TreeUtil

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
   
solution = Solution()
l = [6,2,8,0,4,7,9,None,None,3,5]
root = TreeUtil.build_tree(l)
p = TreeNode(2)
q = TreeNode(8)
TreeUtil.print_tree(solution.lowestCommonAncestor(root, p, q))
print("-" * 20)
l = [6,2,8,0,4,7,9,None,None,3,5]
root = TreeUtil.build_tree(l)
p = TreeNode(2)
q = TreeNode(4)
TreeUtil.print_tree(solution.lowestCommonAncestor(root, p, q))
print("-" * 20)
l = [2,1]
root = TreeUtil.build_tree(l)
p = TreeNode(2)
q = TreeNode(1)
TreeUtil.print_tree(solution.lowestCommonAncestor(root, p, q))

            
"""
Time Complexity: O(H), the worst case is that we must traverse the entire height to find the LCA
Space Complexity: O(1), as no extra space is required
"""