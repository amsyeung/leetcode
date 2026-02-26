"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

from typing import Counter

class Solution: 
    """ 
    This solution is failed due to time limited exceeded. 
    Creating Counter() in each iteration and using it for subtraction are costly.
    Also, segment for s[r:l+1] will create a new string that slows down the process
    """
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = ""
        for r, n in enumerate(s):
            if Counter(n) - Counter(t):
                continue    
            while (Counter(t) - Counter(s[r:l+1])):
                if l < len(s):
                    l += 1
                else:
                    break
            if not (Counter(t) - Counter(s[r:l+1])) and (not res or len(s[r:l+1]) < len(res)):
                res = s[r:l+1]
        return res

class Solution1:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}
        l = 0
        match_count = 0
        res = ""
        min_len = float('inf')
        for r, char in enumerate(s):
            window[char] = window.get(char, 0) + 1
            if char in need and window[char] == need[char]:
                match_count += 1
            while match_count == len(need):
                window_size = r - l + 1
                if window_size < min_len:
                    min_len = window_size
                    res = s[l:r+1]
                
                out_char = s[l]
                """
                reduce the match_count only when removing out the last matched character
                if t = "A", s = "AAC", match_count = 1 as only one "A" in t
                remove out s[l], s becomes "AC", match_count = 1
                remove out s[l] again, s becomes "C", only last A will be removed so we need to match_count - 1
                """
                if out_char in need and window[out_char] == need[out_char]:
                    match_count -= 1
                
                window[out_char] -= 1
                l += 1
        return res


solution = Solution1()
print(solution.minWindow("ADOBECODEBANC", "ABC")) # "BANC"

"""
Time Complexity: O(m + n), since each character is visited, added, and removed from the window exactly once, the sliding window process = O(m), plus O(n) for initialize map by Counter
Space Complexity: O(k), it typically defines as O(1) because need and window only store O(26) for lowercase or O(52) for lowercase + uppercase
"""