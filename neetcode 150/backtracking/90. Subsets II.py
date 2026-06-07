"""
90. Subsets II
Medium
Topics
premium lock icon
Companies
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
"""

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(start: int, cur: List):
            res.append(cur.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                cur.append(nums[i])
                dfs(i + 1, cur)
                cur.pop()
        dfs(0, [])
        return res
    
s = Solution()
print(s.subsetsWithDup([1, 2, 2])) # [[],[1],[1,2],[1,2,2],[2],[2,2]]

"""
Intuition:
i > start ensures we skip duplicates at the same decision level.
We only allow unique numbers in the same level to avoid duplicate subsets.

Time: O(2^N)
Space: O(N)
"""