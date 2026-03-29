"""
190. Reverse Bits
Easy
Topics
premium lock icon
Companies
Reverse bits of a given 32 bits signed integer.

 

Example 1:

Input: n = 43261596

Output: 964176192

Explanation:

Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000
Example 2:

Input: n = 2147483644

Output: 1073741822

Explanation:

Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            b = (n >> i) & 1 # extract the bit
            if b == 1:
               res |= (1 << (31 - i)) # set the corresponding bit
        return res
    
solution = Solution()
print(solution.reverseBits(43261596)) # 964176192

"""
Time Complexity: O(1)
Space Complexity: O(1)
"""
