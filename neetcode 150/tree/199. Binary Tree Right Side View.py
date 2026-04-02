"""
199. Binary Tree Right Side View
Medium
Topics
premium lock icon
Companies
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 

Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:



Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:



Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []
"""

from typing import List, Optional
from treeutil import TreeUtil, TreeNode

class Solution: # failed
    res = []
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def a(node):
            if not node:
                return -1
            l = a(node.left)
            r = a(node.right)
            if r == -1 and l != -1: 
                self.res += l
            elif r != -1:
                self.res += r
            return [node.val] + self.res
        return [root.val] + a(root.right) if root and root.right else []
    
class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):
                res.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res
    
solution = Solution2()
root = TreeUtil.build_tree([1,2,3,None,5,None,4])
print(solution.rightSideView(root)) # [1, 3, 4]
root = TreeUtil.build_tree([1,2,3,4,None,None,None,5]) 
print(solution.rightSideView(root)) # [1, 3, 4, 5]
root = TreeUtil.build_tree([1, None, 3]) 
print(solution.rightSideView(root)) # [1, 3]
root = TreeUtil.build_tree([]) 
print(solution.rightSideView(root)) # []

"""
Time Complexity: O(N), each node visit once
Space Complexity: O(H)
"""


