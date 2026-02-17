"""
739. Daily Temperatures
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

from typing import List

class Solution: # Time Limit Exceeded, first attempt
    def dailyTemperature(self, temperatures: List[int]) -> int:
        res = []
        l, r = 0, 1
        n = len(temperatures)
        if n <= 1:
            return [0]
        while l < n:
            if r > n - 1:
                res.append(0)
            elif temperatures[l] >= temperatures[r]:
                r += 1
                continue
            else:
                res.append(r - l)
            l, r = l + 1, l + 2
        return res
    
class Solution2:
    def dailyTemperature(self, temperatures: List[int]) -> int:
        stack = []
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res

solution = Solution2()
print(solution.dailyTemperature([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]
print(solution.dailyTemperature([30,40,50,60])) # [1,1,1,0]
print(solution.dailyTemperature([30,60,90])) # [1,1,0]

"""
Time Complexity: O(n), n times for appending stack, and n times for while loop (because the index stored in stack will pop away)
Space Complexity: O(n), because when no higher temperatures occur, len(stack) = len(temperatures)
"""