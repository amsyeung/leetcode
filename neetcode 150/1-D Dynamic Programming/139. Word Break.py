"""
139. Word Break
Medium
Topics
premium lock icon
Companies
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[n]
    
solution = Solution()
print(solution.wordBreak("leetcode", ["leet", "code"])) # True
print(solution.wordBreak("applepenapple", ["apple","pen"])) # True
print(solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"])) # False

"""
Time Complexity: O(n^3), O(n) for outer loop + O(n) for inner loop + O(n) for slicing
Space Complexity: O(n) for dp array
"""
