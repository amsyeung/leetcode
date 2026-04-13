"""
300. Longest Increasing Subsequence
Medium
Topics
premium lock icon
Companies
Given an integer array nums, return the length of the longest strictly increasing subsequence.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""

from typing import List

class Solution: # Time: O(n^2), Space: O(n)
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    # i.e. dp[0] = 1, dp[1] = dp[0] + 1, dp[2] = dp[1] + 1
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
    
solution = Solution()
print(solution.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4
print(solution.lengthOfLIS([0,1,0,3,2,3])) # 4
print(solution.lengthOfLIS([7,7,7,7,7,7,7])) # 1