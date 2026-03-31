"""
371. Sum of Two Integers
Solved
Medium
Topics
premium lock icon
Companies
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask # a: sum without carry, b: carry
        return a if a <= MAX else ~(a ^ mask)
    
solution = Solution()
print(solution.getSum(1, 2)) # 3
print(solution.getSum(2, 3)) # 5

"""
Time Complexity: O(1)
Space Complexity: O(1)
"""
