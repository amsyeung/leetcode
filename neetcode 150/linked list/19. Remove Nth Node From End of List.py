"""
19. Remove Nth Node From End of List
Medium
Topics
premium lock icon
Companies
Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
"""

from typing import Optional
from util import ListNode, print_list

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

    
solution = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print_list(solution.removeNthFromEnd(head, 2)) # 1 -> 2 -> 3 -> 5
head = ListNode(1)
print_list(solution.removeNthFromEnd(head, 1)) # None
head = ListNode(1)
head.next = ListNode(2)
print_list(solution.removeNthFromEnd(head, 1)) # 1

"""
Time Complexity: O(n)
Space Complextiy: O(1), only `slow` and `fast` pointer variables
"""