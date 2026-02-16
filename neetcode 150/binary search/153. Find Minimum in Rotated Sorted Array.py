"""
153. Find Minimum in Rotated Sorted Array
Solved
Medium
Topics
premium lock icon
Companies
Hint
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]: # if true, that means the gap (e.g. [...,5,1...] is the gap for first case) should locate at the right side
                l = m + 1
            elif nums[m] < nums[r]: # otherwise, the gap should locate at the left side
                r = m
        return nums[l]
    
solution = Solution()
print(solution.findMin([3,4,5,1,2])) # 1
print(solution.findMin([4,5,6,7,0,1,2])) # 0
print(solution.findMin([11,13,15,17])) # 11

"""
Time Complexity: O(logn) due to binary search
Space Complexity: O(1), only `l`, `r` these variables

Additional notes:
This question is interesting because it seems like Circular Array used for storing data within a limited space.
Think about a situion, [m0, m1, m2, m3, ..., mn] which mx stores the logs, the size of the array will not be increased,
thereby m0 will be replaced by new data and so on. The tricky point is that the gap between, let say the latest data
replaced m3, then m4 will be the oldest record remained. Very brilliant design:)
"""