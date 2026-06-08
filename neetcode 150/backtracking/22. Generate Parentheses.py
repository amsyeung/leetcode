"""
22. Generate Parentheses
Medium
Topics
premium lock icon
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(cur: str, open: int, close: int):
            if len(cur) == 2*n:
                res.append(cur)
            if open < n:
                dfs(cur + "(", open + 1, close)
            if close < open:
                dfs(cur + ")", open, close + 1)
        dfs("", 0, 0)
        return res
        
    
s = Solution()
print(s.generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]

"""
Intuition:
String concatenation (cur + "(") creates a new string, leaving original unchanged.
This acts as implicit backtracking
We add "(" if open < n, and ")" if close < open.

Time: O(4^n / sqrt(n))  Catalan number
Space: O(n), len(cur) == 2*n -> O(2n) -> O(n)
"""