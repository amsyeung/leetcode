"""
25. Reverse Nodes in k-Group
Hard
Topics
premium lock icon
Companies
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""

from typing import Optional
from listutil import ListNode, print_list
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        
        def get_kth(node: Optional[ListNode], k: int) -> Optional[ListNode]:
            while node and k > 0:
                node = node.next
                k -= 1
            return node
        
        dummy = ListNode()
        dummy.next = head
        groupPrev = dummy
        kth = None
        groupNext = None
        
        while True:
            kth = get_kth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            kth.next = None # seperate lists
            newHead = reverse(groupPrev.next)
            oldHead = groupPrev.next
            groupPrev.next = newHead
            oldHead.next = groupNext
            groupPrev = oldHead
        return dummy.next
        
solution = Solution()
nodes = [1, 2, 3, 4, 5]
head = ListNode(nodes[0]) 
cur = head
for node in nodes[1:]:
    cur.next = ListNode(node)
    cur = cur.next
new_head = solution.reverseKGroup(head, 2)
print_list(new_head)

"""
Time: O(n), visit each node once only in reverse() and get_kth()
Space: O(1), only dummy, groupPrev, groupNext pointers
"""