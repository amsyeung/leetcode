"""
152. Maximum Product Subarray
Medium
Topics
premium lock icon
Companies
Given an integer array nums, find a subarray that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that element.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max, dp_min = [0] * n, [0] * n
        dp_max[0], dp_min[0] = nums[0], nums[0]
        res = nums[0]
        for i in range(1, n):
            cand1 = nums[i] * dp_max[i-1]
            cand2 = nums[i] * dp_min[i-1]
            
            dp_max[i] = max(nums[i], cand1, cand2)
            dp_min[i] = min(nums[i], cand1, cand2)
            
            res = max(res, dp_max[i])
        return res
    
solution = Solution()
print(solution.maxProduct([2,3,-2,4])) # 6
print(solution.maxProduct([-2,0,-1])) # 0

"""
Time Complexity: O(n), iteration from 1 to n-1
Space Complexity: O(n), O(n) stores dp_max + O(n) stores dp_min -> O(2n) -> O(n)
"""
