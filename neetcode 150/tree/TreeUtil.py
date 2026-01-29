from typing import Optional, List

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
        if not nodes:
            return None
        iter_nodes = [TreeNode(val) if val is not None else None for val in nodes]
        for i in range(len(iter_nodes)):
            if iter_nodes[i] is not None:
                left_idx = 2 * i + 1
                right_idx = 2 * i + 2
                if left_idx < len(iter_nodes):
                    iter_nodes[i].left = iter_nodes[left_idx]
                if right_idx < len(iter_nodes):
                    iter_nodes[i].right = iter_nodes[right_idx]
        return iter_nodes[0] # return head

    @staticmethod
    def print_tree(node, level=0):
        if node:
            TreeUtil.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '-> ' + str(node.val))
            TreeUtil.print_tree(node.left, level + 1)