"""
141. Linked List Cycle
Solved
Easy
Topics
premium lock icon
Companies
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""

from util import ListNode
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

solution = Solution()
head = ListNode(3)
head.next = ListNode(2)
tmp = head.next
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = tmp
print(solution.hasCycle(head)) # True
head = ListNode(1)
head.next = ListNode(2)
tmp = head.next
head.next.next = tmp
print(solution.hasCycle(head)) # True
head = ListNode(1)
print(solution.hasCycle(head)) # False

"""
Time Complexity: O(n)
Space Complexity: O(1), only slow, fast pointers
"""