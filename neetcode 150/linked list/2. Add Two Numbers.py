"""
2. Add Two Numbers
Medium
Topics
premium lock icon
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

from util import ListNode, print_list
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        r1 = l1
        r2 = l2
        s1, s2 = 0, 0
        n = 0
        while r1:
            s1 += r1.val * 10 ** n
            r1 = r1.next
            n += 1
        n = 0
        while r2:
            s2 += r2.val * 10 ** n
            r2 = r2.next
            n += 1
        
        s3 = s1 + s2
        if s3 == 0:
            return dummy
        p = dummy
        while s3 > 0:
            remain = s3 % 10
            s3 = s3 // 10
            p.next = ListNode(remain)
            p = p.next
        return dummy.next
        
class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        v1, v2 = 0, 0
        s = 0
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry
            carry = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next

solution = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print_list(solution.addTwoNumbers(l1, l2))

solution2 = Solution2()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
print_list(solution2.addTwoNumbers(l1, l2))
"""
Time Complexity: O(n)
Space Complexity: O(1)
"""