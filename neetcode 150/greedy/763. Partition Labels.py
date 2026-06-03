"""
763. Partition Labels
Medium
Topics
premium lock icon
Companies
Hint
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
"""

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occurrence = {}
        for i, c in enumerate(s):
            last_occurrence[c] = i
        
        res = []
        start = 0
        end = 0
        for i, c in enumerate(s):
            end = max(end, last_occurrence[c])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res

solution = Solution()
print(solution.partitionLabels("ababcbacadefegdehijhklij")) # [9, 7, 8]

"""
Time: O(n)
Space: O(1), max(len(last_occurrence)) ~= 26 characters
"""