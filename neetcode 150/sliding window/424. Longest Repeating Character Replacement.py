"""
424. Longest Repeating Character Replacement
Solved
Medium
Topics
premium lock icon
Companies
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
"""

class Solution:
    def characterReplacement(self, s: str, k:int) -> int:
        l= 0
        res = 0
        max_f = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_f = max(max_f, count[s[r]])
            while r - l + 1 - max_f > k: # (r - l + 1) is window-size, (window_size - max_f) obtains the number of characters can be changed
                count[s[l]] -= 1 # since the window no longer valid, we need to move our window. The count of the most left-side character should be minus 1
                l += 1 # move our window
            res = max(res, r - l + 1) # the question require an answer of the longest substring containing the same letter, which means the window size
        return res
    
solution = Solution()
print(solution.characterReplacement("ABAB", 2)) # 4
print(solution.characterReplacement("AABABBA", 1)) # 4

"""
Time Complexity: O(n), n times iterates through the string, and inside the while loop, left pointer only moves forward and never retreats, meaning each character is visied at most twice -> O(n)
Space Complexity: O(1), this case only involves uppercase characters, therefore, auxiliary complexity depends on 26 characters, which is constant -> O(1)
"""