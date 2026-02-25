"""
102. Binary Tree Level Order Traversal
Medium
Topics
premium lock icon
Companies
Hint
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
"""

from typing import List, Optional
from treeutil import TreeNode, TreeUtil
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            level_size = len(queue)
            current_level = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(current_level)
        return res
    
solution = Solution()
l = [3,9,20,None,None,15,7]
root = TreeUtil.build_tree(l)
print(solution.levelOrder(root)) # [[3],[9,20],[15,7]]
l = [1]
root = TreeUtil.build_tree(l)
print(solution.levelOrder(root)) # [[1]]
l = []
root = TreeUtil.build_tree(l)
print(solution.levelOrder(root)) # []

"""
Time Complexity: O(N), because we must visit every node exactly once to build the level-order lists
Space Complexity: O(N), in the worst case, the queue will store nodes proportional to the maximum
                    width of the tree, and the final result list stores all N node values
"""