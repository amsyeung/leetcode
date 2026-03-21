"""
746. Min Cost Climbing Stairs
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

 

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""

from typing import List

class Solution: # Time: O(n), Space: O(n)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1): # (n + 1) is the top
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]

class Solution2: # Time: O(n), Space: O(1)
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev1, prev2 = 0, 0
        cur = 0
        for i in range(2, n + 1):
            cur = min(prev1 + cost[i-1], prev2 + cost[i-2])
            prev1, prev2 = cur, prev1
        return cur

solution = Solution2()
print(solution.minCostClimbingStairs([10,15,20])) # 15
