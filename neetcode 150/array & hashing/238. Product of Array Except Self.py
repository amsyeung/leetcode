"""
238. Product of Array Except Self
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""

from typing import List
import math

class Solution: # Time Limit Exceeded
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            res = (math.prod(nums[:i]) if nums[:i] else 1) * math.prod(nums[i+1:])
            ans.append(res)
        return ans
    
class Solution2: # called Prefix/Suffix Sum
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for j in range(n - 1, -1, -1):
            res[j] *= postfix
            postfix *= nums[j]
        return res
        
solution = Solution2()
print(solution.productExceptSelf([1,2,3,4])) # [24, 12, 8, 6]
print(solution.productExceptSelf([-1, 1, 0, -3, 3])) # [0, 0, 9, 0, 0]

"""
Time Complexity: O(n) for the first loop to calculate nums[0] * ... * nums[i-1]
                 + O(n) for the second loop to calculate nums[i+1] * ... * nums[n-1]
                 = O(n)
                 
Space Complexity: O(1), only prefix and postfix variables, constant 
"""