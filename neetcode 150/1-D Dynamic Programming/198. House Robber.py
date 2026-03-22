"""
198. House Robber
Medium
Topics
premium lock icon
Companies
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

from typing import List

class Solution: # Time: O(n), Space: O(n)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        d = [0] * n
        d[0], d[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            d[i] = max(d[i-1], d[i-2] + nums[i])
        return d[n-1]
    
class Solution2: # Time: O(n), Space: O(1)
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        prev1, prev2 = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            prev1, prev2 = prev2, max(prev2, prev1 + nums[i])
        return prev2
    
solution = Solution2()
print(solution.rob([1,2,3,1])) # 4
print(solution.rob([1,100,1])) # 4
