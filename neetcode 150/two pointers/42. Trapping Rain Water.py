"""
42. Trapping Rain Water
Hard
Topics
premium lock icon
Companies
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        l, r = 0, 0
        n = len(height)
        while l < n - 1:
            while l < n and height[l] == 0:
                l += 1
            while ((l + 1) < (n - 1)) and height[l + 1] > height[l]:
                l += 1
                
            r = l + 1
            while r < (n - 1) and height[r] < height[l] and height[r] < max(height[l+1:n]):
                r += 1
            if height[l+1:r] and max(height[l+1:r]) > min(height[l], height[r]):
                l += 1
                continue
            s = 0
            signed = -1
            for i in range(l + 1, r): # sum all blocks in between
                t = 0
                if height[i] > 0:
                    t = signed * height[i]
                s += min(height[l], height[r]) + t
            total += s
            l = r        
        return total

solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(solution.trap([4,2,0,3,2,5])) # 9
print(solution.trap([4,2,3])) # 1
print(solution.trap([4,9,4,5,3,2])) # 1
print(solution.trap([0,0,0])) # 0


"""
Time Complexity: O(n^2)
Space Complexity: O(1)
"""