"""
40. Combination Sum II
Medium
Topics
premium lock icon
Companies
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
"""

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(start: int, cur: List, total: int) -> None:
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i])
                cur.pop()
        dfs(0, [], 0)
        return res

s = Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8)) # [[1,1,6], [1,2,5], [1,7], [2,6]]

"""
Intuition:
- Sort candidates to allow pruning and duplicate skipping.
- If total + candidates[i] > target: break (prune, rest are larger).
- i > start skips duplicates at same level to avoid duplicate results.
- Each number used once: dfs(i+1).

Time: O(2^N)
Space: O(N)
"""
