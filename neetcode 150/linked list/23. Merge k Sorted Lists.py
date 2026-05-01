"""
23. Merge k Sorted Lists
Hard
Topics
premium lock icon
Companies
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
"""

from typing import Optional, List
from listutil import ListNode, print_list
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i in range(len(lists)):
          node = lists[i]
          if node:
            heapq.heappush(min_heap, (node.val, i, node)) # 1 1 2
        dummy = ListNode()
        tail = dummy
        while min_heap:
          _, i, min_node = heapq.heappop(min_heap)
          tail.next = min_node
          tail = tail.next
          if min_node.next:
            heapq.heappush(min_heap, (min_node.next.val, i, min_node.next))
        return dummy.next
        
      
solution = Solution()
l = []
h1 = ListNode(1)
h1.next = ListNode(4)
h1.next.next = ListNode(5)
l.append(h1)
h2 = ListNode(1)
h2.next = ListNode(3)
h2.next.next = ListNode(4)
l.append(h2)
h3 = ListNode(2)
h3.next = ListNode(6)
l.append(h3)
print_list(solution.mergeKLists(l)) # [1,1,2,3,4,4,5,6]

"""
Time: O(N log K), where N is total number of nodes across all k lists
Space: O(k), due to the min-heap holding at most one node from each list
"""