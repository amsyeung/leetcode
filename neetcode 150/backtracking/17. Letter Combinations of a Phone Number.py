"""
17. Letter Combinations of a Phone Number
Medium
Topics
premium lock icon
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
"""

from collections import defaultdict
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(idx: int, path: str):
            if idx == len(digits):
                res.append(path)
                return
            for c in phone[digits[idx]]:
                dfs(idx + 1, path + c)
        dfs(0, "")
        return res

s = Solution()
print(s.letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]

"""
Intuition:
`idx` tracks which digit we are processing. We concatenate letters to build combinations until the string length equals len(digits).

Time: 
O(3^m * 4^n)
m = number of digits mapping to 3 letters (2,3,4,5,6,8)
n = number of digits mapping to 4 letters (7,9)
The worst case is O(4^n) if all digits only contain 7,9

Space: O(n), n = len(digits)
"""