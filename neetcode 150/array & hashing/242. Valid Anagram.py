"""
242. Valid Anagram
Solved
Easy
Topics
premium lock icon
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

class Solution:
    def count(self, s: str) -> dict:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]] += 1
            else:
                d[s[i]] = 1
        return d
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # print(f"s: {self.count(s)}")
        # print(f"t: {self.count(t)}")
        return self.count(s) == self.count(t)
    
solution = Solution()
print(solution.isAnagram("anagram", "nagaram")) # true
print(solution.isAnagram("rat", "car")) # false
print(solution.isAnagram("a", "ab")) # false

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""