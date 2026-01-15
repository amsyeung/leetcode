"""
15. 3Sum
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List

# naive solution (brute force)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        n = len(nums)
        for i in range(n):
            for j in range(1, n):
                for k in range(2, n):
                    res = nums[i] + nums[j] + nums[k]
                    valid = i != j and i != k and j != k
                    if res == 0 and valid:
                        s.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return s
    
# solution = Solution()
# print(solution.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
        
# Using two pointers
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # O(nlogn)
        n = len(nums)
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:            
                total = nums[i] + nums[l] + nums[r]
                if total < 0: # a larger nums[l], move towards left
                    l += 1
                elif total > 0: # a smaller nums[r], move towards right
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while nums[l] == nums[l + 1] and l < r: # skip the second element duplicate
                       l += 1
                    while nums[r] == nums[r - 1] and l < r: # skip the third element duplicate
                        r -= 1
                    l += 1
                    r -= 1      
        return res
    
    
solution2 = Solution2()
print(solution2.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]

"""
Time Complexity: O(nlogn) for sorting + O(n^2), because n times with outer loop and inner two pointers loop n times
Space Complexity: Python Timsort consumes O(logn) to O(n), so approximately O(logn) to O(n)
"""