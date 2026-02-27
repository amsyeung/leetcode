"""
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

from typing import List
from collections import deque

class Solution: # Time Limit Exceeded
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        n = len(nums)
        for r in range(n):
            window_size = r - l + 1
            if window_size == k:
                res.append(max(nums[l:r+1]))
                l += 1
        return res
    
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        res = []
        for r, num in enumerate(nums):
            # pop out all values which are smaller than nums[r]
            while q and nums[q[-1]] < num:
                q.pop()
            q.append(r)
            # (r - k + 1) is the left boundary of the current window
            if q[0] < r - k + 1:
                q.popleft()
            # the window size >= k, append the maximum value of the current window which is the head of the list
            if r >= k - 1:
                res.append(nums[q[0]])
        return res
    
solution = Solution2()
print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)) # [3,3,5,5,6,7]
print(solution.maxSlidingWindow([1], 1)) # [1]

"""
Time Complexity: O(n), each element is added and removed from the queue at most once
Space Complexity: O(k), if deque is [10, 9, 8, 7, ...], where k = window size
"""