"""
297. Serialize and Deserialize Binary Tree
Hard
Topics
premium lock icon
Companies
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

 

Example 1:


Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []
Output: []
"""

from collections import deque
from typing import Optional
from treeutil import TreeNode, TreeUtil

class Codec:
    def serialize(self, root: TreeNode) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = deque(data.split(","))
        def dfs():
            v = vals.popleft()
            if v == "N":
                return None
            node = TreeNode(int(v))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

ser = Codec()
deser = Codec()
root = TreeUtil.build_tree([1,2,3,None,None,4,5])
ans = deser.deserialize(ser.serialize(root))
TreeUtil.print_tree(ans) # [1,2,3,None,None,4,5]

"""
Time:
    - serialize: O(n) for each node
    - deseralize: O(n) for each token
Space:
    - serialize: O(n) for res + O(h) for recursion stack -> O(n)
    - deserialize: O(n) for token + O(h) recursion stack -> O(n)
        where h is tree height, balanced: O(log n) and worst case (skewed): O(n)
"""