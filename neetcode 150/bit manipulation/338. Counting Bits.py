"""
338. Counting Bits
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        l = []
        for i in range(n + 1):
            l.append(list(f"{i:b}").count("1"))
        return l
    
solution = Solution()
print(solution.countBits(5)) # [0,1,1,2,1,2]

"""
Time Complexity: O(n), n times iterations
Space Complexity: O(n), list stores each individual count of "1"
"""