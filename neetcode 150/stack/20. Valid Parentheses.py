"""
20. Valid Parentheses
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        map = { "[": "]", "{": "}", "(": ")" }
        arr = []
        if len(s) < 2:
            return False
        for c in s:
            if c in map: # if c is one of the key
                arr.append(c)
            else:
                if not arr:
                    return False
                n = arr.pop()
                if map[n] != c:
                    return False
        if arr:
            return False
        return True
    
class Solution2:
    def isValid(self, s: str) -> bool:
        d = { ")": "(", "}": "{", "]": "[" }
        stack = []
        for c in s:
            if c in d:
                top_element = stack.pop() if stack else "#"
                if d[c] != top_element:
                    return False
            else:
                stack.append(c)
        return not stack
                
solution = Solution2()
print(solution.isValid("()")) # True
print(solution.isValid("()[]{}")) # True
print(solution.isValid("(]")) # False
print(solution.isValid("([])")) # True
print(solution.isValid("([)]")) # False
print(solution.isValid("((")) # False

"""
Time Complexity: O(n), where n is len(s)
Space Complexity: O(n) when no match, the stack will store every single character from the string
"""
