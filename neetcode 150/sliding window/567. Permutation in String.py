"""
567. Permutation in String
Medium
Topics
premium lock icon
Companies
Hint
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        # impossible to make s2 transform to s1
        if n1 > n2:
            return False
        s1_count = [0] * 26
        s2_count = [0] * 26
        # only count the first window, 0 to (n1 - 1)
        for i in range(n1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        if s1_count == s2_count:
            return True
        # sliding the window and compare their (s1, s2) occurrence of alpha character
        for i in range(n1, n2):
            s2_count[ord(s2[i]) - ord('a')] += 1
            s2_count[ord(s2[i - n1]) - ord('a')] -= 1
            if s1_count == s2_count:
                return True
        return False
    
solution = Solution()
print(solution.checkInclusion("ab", "eidbaooo")) # True
print(solution.checkInclusion("ab", "eidboaoo")) # False

"""
Time Complexity: O(n), where n hinges on the size of s2 because s2 >= s1 normally
Space Complexity: O(1), because only 26 characters will be stored into s1_count and s2_count, constant space
"""