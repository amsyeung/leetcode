"""
54. Spiral Matrix
Medium
Topics
premium lock icon
Companies
Hint
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List

class Solution: # Time: O(m * n), Space: O(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        res = []
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if not (left <= right and top <= bottom):
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res

solution = Solution()
print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])) # [1,2,3,6,9,8,7,4,5] 
print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])) # [1,2,3,4,8,12,11,10,9,5,6,7]