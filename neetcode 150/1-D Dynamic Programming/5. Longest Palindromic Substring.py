"""
5. Longest Palindromic Substring
Medium
Topics
premium lock icon
Companies
Hint
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r] # when the loop is end, l and r pointers always jump one more step, that's why step back in here
        for i in range(len(s)):
            s1 = expand(i, i)
            s2 = expand(i, i + 1)
            res = max(res, s1, s2, key=len)
        return res
        
    
solution = Solution()
print(solution.longestPalindrome("babad")) # "bab"
print(solution.longestPalindrome("cbbd")) # "bb"

"""
Time Complexity: O(N^2), where n times for the for loop and n times called expand() when the worst case would happen ("aaaaaa")
Space Complexity: O(1), only l, r, i variables
"""

