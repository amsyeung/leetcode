"""
73. Set Matrix Zeroes
Medium
Topics
premium lock icon
Companies
Hint
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
"""

from typing import List

class Solution:
    def setZeros(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = False
        first_col_has_zero = False
        for i in range(n):
            if matrix[0][i] == 0:
                first_row_has_zero = True
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if first_row_has_zero:
            for i in range(n):
                matrix[0][i] = 0
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0

solution = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
solution.setZeros(matrix) # [[1,0,1],[0,0,0],[1,0,1]]
print(matrix)

"""
Time Complexity: O(m * n)
Space Complexity: O(1)
"""