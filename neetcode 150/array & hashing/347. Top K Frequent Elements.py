"""
347. Top K Frequent Elements
Medium
Topics
premium lock icon
Companies
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]
"""

from typing import List
from collections import Counter
import heapq

class Solution: # Time: O(NlogN) if all values are distinct, Space: O(N)
    def topkFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        res = []
        for num in nums:
            map[num] = map.get(num, 0) + 1
        items = list(map.items())
        items.sort(key=lambda x: x[1], reverse=True)
        # print(items)
        for i in range(k):
            res.append(items[i][0])
        return res
    
class Solution2: # Time: O(NlogK), Space: O(N) 
    def topkFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [item[0] for item in count.most_common(k)]
    
class Solution3: # Time: O(NlogK), Space: O(N + K) -> O(N) because N >= K
    def topkFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) >= 3:
                heapq.heappop(heap)
        return [item[1] for item in heap]
        

solution = Solution3()
print(solution.topkFrequent([1,1,1,2,2,3], 2)) # [1, 2]
print(solution.topkFrequent([1], 1)) # [1]
print(solution.topkFrequent([1,2,1,2,1,2,3,1,3,2], 2)) # [1, 2]
print(solution.topkFrequent([3,0,1,0], 1)) # [0]
