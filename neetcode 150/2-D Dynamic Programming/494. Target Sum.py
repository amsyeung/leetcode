"""
494. Target Sum
Medium
Topics
premium lock icon
Companies
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
"""

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        
        if (target + total_sum) % 2 != 0 or abs(target) > total_sum:
            return 0
        
        P = (target + total_sum) // 2
        n = len(nums)
        
        dp = [[0] * (P + 1) for _ in range(n + 1)]
        
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(P + 1):
                not_choose = dp[i - 1][j]
                if j >= num:
                    choose = dp[i - 1][j - num]
                else:
                    choose = 0
                dp[i][j] = not_choose + choose
        return dp[n][P]
    
s = Solution()
print(s.findTargetSumWays([1,1,1,1,1], 3)) # 5
print(s.findTargetSumWays([1], 1)) # 1

"""
Time: O(n * P)
Space: O(n * P)
"""