"""
309. Best Time to Buy and Sell Stock with Cooldown
Medium
Topics
premium lock icon
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp0 = -prices[0]
        dp1 = float('-inf')
        dp2 = 0
        
        for i in range(1, n):
            new0 = max(dp0, dp2 - prices[i])
            new1 = dp0 + prices[i]
            new2 = max(dp1, dp2)
            dp0, dp1, dp2 = new0, new1, new2
            
        return max(dp1, dp2)
    
s = Solution()
print(s.maxProfit([1,2,3,0,2])) # 3

"""
Intuition:
We split stock operations into 3 independent daily states to handle the cooldown rule:
1. Hold stock (dp0): We either keep holding from previous day, or buy new stock only if previous day is free of cooldown.
2. Sold stock today (dp1): Can only transition from holding stock yesterday; selling triggers a 1-day cooldown.
3. Free empty hand (dp2): Either we finished cooldown after selling yesterday, or we stayed empty-handed before.

We only keep three rolling variables instead of an n-length DP array to save space.
After processing all days, the maximum profit must come from empty-hand states (dp1 or dp2), since holding stock at the end cannot yield optimal profit.

Time Complexity: O(n)
We iterate through all prices once with constant work per day.

Space Complexity: O(1)
Only three variables store previous states; no extra array proportional to input size.
"""