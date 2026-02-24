"""
1. Two Sum
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in map:
                return [map[complement], i]
            map[n] = i

solution = Solution()
print(solution.twoSum([2,7,11,15], 9)) # [0, 1]
print(solution.twoSum([3,2,4], 6)) # [1, 2]
print(solution.twoSum([3,3], 6)) # [0, 1]

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
