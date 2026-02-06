"""
49. Group Anagrams
Solved
Medium
Topics
premium lock icon
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord[c] - ord['a']] += 1
            res[tuple(count)].append(s)
        return list(res.values())
        
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])) # [["bat"],["nat","tan"],["ate","eat","tea"]]
print(solution.groupAnagrams([""])) # [[""]]
print(solution.groupAnagrams(["a"])) # [["a"]]

"""
Time Complexity: O(K * N), where K = the number of elements and N = 26 times for maximum (A-Z), O(K * 26) -> O(K)
Space Complexity: the worst case happen when no matches, then depends on the size of `strs`, O(K)
"""
