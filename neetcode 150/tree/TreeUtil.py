from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f"Node({self.val})"

class TreeUtil:
    @staticmethod
    def build_tree(nodes: List[int]) -> Optional[TreeNode]:
        if not nodes: return None
        root = TreeNode(nodes[0])
        queue = deque([root]) 
        i = 1 
        while queue and i < len(nodes):
            current = queue.popleft()
            # handle left child
            if i < len(nodes):
                if nodes[i] is not None:
                    current.left = TreeNode(nodes[i])
                    queue.append(current.left)
                i += 1
            # handle right child
            if i < len(nodes):
                if nodes[i] is not None:
                    current.right = TreeNode(nodes[i])
                    queue.append(current.right)
                i += 1
        return root

    @staticmethod
    def print_tree(node, level=0):
        if node:
            TreeUtil.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.val))
            TreeUtil.print_tree(node.left, level + 1)