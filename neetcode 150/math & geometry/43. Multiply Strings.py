"""
43. Multiply Strings
Medium
Topics
premium lock icon
Companies
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m = len(num1)
        n = len(num2)
        res = [0] * (m + n)
        for i in range(m - 1, -1, -1):
            d1 = int(num1[i])
            for j in range(n - 1, -1, -1):
                d2 = int(num2[j])
                product = d1 * d2
                tens = i + j
                ones = i + j + 1
                total = product + res[ones]
                res[ones] = total % 10
                res[tens] += total // 10
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
        return "".join(str(x) for x in res[start:])
    
s = Solution()
print(s.multiply("2", "3")) # "6"
print(s.multiply("123", "456")) # "56088"
print(s.multiply("99", "99")) # "9801"

"""
Intuition:
Intuition:
An m-digit number multiplied by an n-digit number yields at most m+n digits.
We store multiplication results in an m+n-length array.
The product of num1[i] and num2[j] stores its units digit at i+j+1 and adds the tens carry to i+j.
Carries are accumulated temporarily and only converted to string at the end after removing leading zeros.

Time: O(m*n)
Space: O(m+n)
"""