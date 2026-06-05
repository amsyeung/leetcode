"""
46. Permutations
Medium
Topics
premium lock icon
Companies
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def dfs(cur: List):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    cur.append(nums[i])
                    dfs(cur)
                    used[i] = False
                    cur.pop()
        dfs([])
        return res

s = Solution()
print(s.permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

"""
Time: O(N * N!)
here are N! permutations, and each takes O(N) to copy into result.

Space: O(N)
Recursion stack depth = N, used array = N space.
"""