"""
84. Largest Rectangle in Histogram
Hard
Topics
premium lock icon
Companies
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for r, height in enumerate(heights + [0]):
            while stack and height < heights[stack[-1]]:
                mid_idx = stack.pop()
                h = heights[mid_idx]
                if not stack:
                    w = r
                else:
                    w = r - stack[-1] - 1
                res = max(res, h * w)
            stack.append(r)
        return res
    
solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,2,3])) # 10

"""
Time Complexity: O(n), O(n) for for-loop + O(n) for while loop -> O(2n) -> O(n)
Space Complexity: O(n), in the worst-case scenario (e.g., when heights is strictly increasing, such as [1, 2, 3, 4, 5]), all indices will be stored in the stack before reaching the final sentinel value 0
Notes:
    the way of calculating the width isn't intuitive, need to draw diagrams
"""