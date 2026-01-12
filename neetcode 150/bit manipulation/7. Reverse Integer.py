"""
7. Reverse Integer
Medium
Topics
premium lock icon
Companies
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        sign = -1 if x < 0 else 1
        s = list(str(abs(x)))
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
        res = sign * int("".join(s))
        if res < INT_MIN or res > INT_MAX:
            return 0
        else:
            return res

class Solution2:
    def reverse(self, x: int) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x:
            pop = x % 10
            x //= 10
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and pop > 7) or (res == INT_MAX // 10 and pop > 8 and sign == -1):
                return 0
            res = res * 10 + pop
        return sign * res

solution = Solution()
print(solution.reverse(123)) # 321
print(solution.reverse(-123)) # -321
print(solution.reverse(120)) # 21

solution = Solution2()
print(solution.reverse(-7463847412)) # 321

"""
Time Complexity: O(n), iterating n characters of list(str(abs(x)))
Space Complexity: O(n), n characters store into list
"""