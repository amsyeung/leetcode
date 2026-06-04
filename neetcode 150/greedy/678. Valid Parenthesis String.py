"""
678. Valid Parenthesis String
Medium
Topics
premium lock icon
Companies
Hint
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        for c in s:
            if c == '(':
                low, high = low + 1, high + 1
            elif c == ')':
                low, high = low - 1, high - 1
            else: # c == '*'
                low -= 1    # '*' treats as ')'
                high += 1   # '*' treats as '('
                
            if high < 0:
                return False
            
            if low < 0:
                low = 0
        return low == 0
        
s = Solution()
print(s.checkValidString("()")) # True
print(s.checkValidString("(*)")) # True
print(s.checkValidString("(*))")) # True
print(s.checkValidString(")*))")) # False
print(s.checkValidString("**))")) # True

"""
Intuition:
To track a possible range [low, high] of open parenthesis count,
low = minimal open brackets (treat * as ')')
high = maximal open brackets (treat * as '(')
- if high < 0: even turning all stars into '(' cannot offset excess ')', return False
- if low < 0: minimal open count cannot be negative, reset low to 0 (abandon the path where too many * are used as ')')

Time: O(n), visit each character
Space: O(1), only low, high variables, constant spaces
"""
