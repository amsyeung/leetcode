"""
215. Kth Largest Element in an Array
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

from typing import List
import heapq

class Solution: # it's the first attempt, not good because this stores all the element in nums 
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        largest = 0
        for num in nums:
            heapq.heappush_max(heap, num)
        for _ in range(k):
            largest = heapq.heappop_max(heap)
        return largest

class Solution2: # only maintain a heap with k size
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heapreplace(heap, nums[i])
        return heap[0]
    
solution = Solution2()
print(solution.findKthLargest([3,2,1,5,6,4], 2)) # 5
print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4

"""
Time Complexity: O(NlogK), O(K) for heapify + O(logK) for every heapreplace (pop and push) with (N - K) times -> + O(K) + (N - K) * O(logK) -> O(NlogK) as N >> K
Space Complexity: O(K), because only maintain a min heap with K size
"""