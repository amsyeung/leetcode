"""
138. Copy List with Random Pointer
Medium
Topics
premium lock icon
Companies
Hint
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
"""

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        old_to_new = {}

        # create nodes
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # connect next and random
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next
        
        return old_to_new[head]

        

solution = Solution()
nodes = [Node(7), Node(13), Node(11), Node(10), Node(1)]

for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

random_indices = [None, 0, 4, 2, 0]

for i, ri in enumerate(random_indices):
    nodes[i].random = nodes[ri] if ri is not None else None

head = nodes[0]

print(solution.copyRandomList(head)) # [[7,None],[13,0],[11,4],[10,2],[1,0]]

"""
Time: O(n), look up all nodes twice
Space: O(n), which stores n items into hashmap

Notes (follow-up later):
    similar questions: leetcode@1851
    O(1) solution: interlearving (pending)
"""