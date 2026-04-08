"""
647. Palindromic Substrings
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""

class Solution: # Time: O(N^2), Space: O(1)
    def countSubstrings(self, s: str) -> int:
        self.res = 0
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                self.res += 1
                l -= 1
                r += 1
        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        return self.res
    
solution = Solution()
print(solution.countSubstrings("abc")) # 3
print(solution.countSubstrings("aaa")) # 6

