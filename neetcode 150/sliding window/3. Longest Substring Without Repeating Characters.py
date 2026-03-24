"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.    
"""
class Solution:
    def lengthOfLongest(self, s: str) -> int:
        l = 0
        res = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
 
solution = Solution()
print(solution.lengthOfLongest("abcabcbb")) # len(abc) = 3
print(solution.lengthOfLongest("bbbbb"))    # len(b) = 1
print(solution.lengthOfLongest("pwwkew"))   # len(wke) = 3

"""
Time Complexity 
   O(n) for looping len(s)
   O(n-1) for n-1 times .remove() + O(n) for n times .add() => O(n-1) + O(n) => 2O(n)
   O(n) for update res variable
   
   O(n + 2n + n) = O(n)
   
Space Complexity
    worse case is no duplicate, charSet stores all the characters, O(n)
"""
