"""
78. Subsets
Medium
Topics
premium lock icon
Companies
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

from typing import List

class Solution: # Cascading
    # Time: O(n * 2^n), 2^n subsets, and for each one, we perform an addition/copy which takes O(n)
    # Space: O(n * 2^n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            new_subsets = []
            for cur in res:
                new_subsets.append(cur + [num]) # clone the current subset and add the new number
            res.extend(new_subsets) # add all the new subsets into res
        return res

class Solution2: # BackTracking
    # Time: O(n * 2^n)
    # Space: O(n), O(n) for storing recursive stacks and O(n/2) for storing subsets -> O(n) + O(n/2) = O(n)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # 1. Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # 2. Exclude nums[i]
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res

solution = Solution2()
print(solution.subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]