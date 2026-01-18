"""
74. Search a 2D Matrix
Solved
Medium
Topics
premium lock icon
Companies
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flatMatrix = sum(matrix, [])
        l, r = 0, len(flatMatrix) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if flatMatrix[mid] == target:
                return True
            elif flatMatrix[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
    
solution = Solution()
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # True
print(solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # False
    
"""
Time Complexity: O(n)
Space Complexity: O(n), n depends on how many element on matrix, because create a copied list into flatMatrix
"""