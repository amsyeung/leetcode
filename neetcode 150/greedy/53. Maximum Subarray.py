"""
53. Maximum Subarray
Medium
Topics
premium lock icon
Companies
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

from typing import List

class Solution: # TLE, Time: O(n^2), Space: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        sum = -float('inf')
        l = 0
        n = len(nums)
        while l < n:
            cur_sum = 0
            for r in range(l, n):
                cur_sum += nums[r]
                sum = max(sum, cur_sum)
                if cur_sum <= 0:
                    cur_sum -= nums[r]
                    l = r
                    break
            l += 1
        return sum
    
class Solution2: # Time: O(n), Space: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -float('inf')
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum > max_sum:
                max_sum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return max_sum
    
solution = Solution2()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(solution.maxSubArray([-1])) # -1