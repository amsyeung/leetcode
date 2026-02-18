"""
143. Reorder List
Medium
Topics
premium lock icon
Companies
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""

from typing import Optional
from util import ListNode, print_list

class Solution:
    def recordList(self, head: Optional[ListNode]) -> None:
        # find the middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_head = slow.next
        slow.next = None
        
        # Reverse second linked list
        prev = None
        cur = second_head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # Merge two linked lists
        first, second = head, prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
            
solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
solution.recordList(head)
print_list(head)

"""
Time Complexity: O(n/2) for finding middle node  + O(n/2) for reserve half of second list + O(n) for merging two lists -> O(n)
Space Complexity: O(1), only pointer variables, constant
"""