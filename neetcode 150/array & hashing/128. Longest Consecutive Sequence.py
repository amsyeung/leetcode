"""
128. Longest Consecutive Sequence
Medium
Topics
premium lock icon
Companies
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:

Input: nums = [1,0,1,2]
Output: 3
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if (num - 1) not in nums:
                n = num
                while (n + 1) in nums:
                    n += 1
                res = max(res, n - num + 1)
        return res
    
solution = Solution()
print(solution.longestConsecutive([100,4,200,1,3,2])) # 4
print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
print(solution.longestConsecutive([1,0,1,2])) # 3

"""
Time Complexity: O(n), O(n) for checking if (num - 1) exists in the set + O(n) for while loop (because not every num will use in this while loop) -> O(2n) = O(n)
Space Complexity: O(n), where set(nums) stores all values
"""