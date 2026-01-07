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

"""
    i + j + k = 0
    i = -k - j
    i = - (k + j)
    k + j = -i
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                    # 1. sort the array
        res = []
        n = len(nums)

        for i in range(n - 2):         # 2. outer loop over first element
            # skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:        # 2. two‑pointer search
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # move both pointers past duplicates
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:         # need a larger sum
                    left += 1
                else:                   # total > 0, need a smaller sum
                    right -= 1

        return res
        # l, r = 0, 0
        # arr = []
        # while (l < len(nums) - 1 and len(nums) >= 3):
        #     if r == len(nums) - 1:
        #         l += 1
        #         r = l
        #     res = -(nums[l] + nums[r])
        #     if res in nums and nums.index(res) not in [l, r] and (l != r and l != nums.index(res) and r != nums.index(res)):
        #         arr.append([nums[l], nums[r], res])
        #     r += 1
        # return arr
solution = Solution()
tmp = solution.threeSum([-1,0,1,2,-1,-4])
print(tmp)
