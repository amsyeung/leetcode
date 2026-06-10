"""
131. Palindrome Partitioning
Medium
Topics
premium lock icon
Companies
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
"""

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        res = []
        def dfs(start: int, cur: List[str]) -> None:
            if start == len(s):
                res.append(cur.copy())
                return
            for i in range(start, len(s)):
                substring = s[start:i+1]
                if is_palindrome(substring):
                    cur.append(substring)
                    dfs(i + 1, cur)
                    cur.pop()
        dfs(0, [])
        return res

s = Solution()
print(s.partition("aab")) # [["a","a","b"],["aa","b"]]

"""
Intuition:
To use backtracking to split the string at each position, 
and only proceed if the current substring is a palindrome

Time: O(N * 2^N) -> 2^N possible partitions, each takes O(N) to check palindrome.
Space: O(N) -> recursion stack depth.
"""