"""
50. Pow(x, n)
Medium
Topics
premium lock icon
Companies
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(base, exp):
            res = 1.0
            while exp > 0:
                # odd
                if exp % 2 == 1:
                    res *= base
                base *= base
                exp = exp // 2
            return res
        if n >= 0:
            return power(x, n)
        else:
            return 1 / power(x, -n)
    
s = Solution()
print(s.myPow(2.00000, 10)) # 1024.00000
print(s.myPow(2.10000, 3)) # 9.26100
print(s.myPow(2.00000, -2)) # 0.25000

"""
Time: O(log|n|), each iteration halves exponent
Space: O(1)
"""