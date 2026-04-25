"""
79. Word Search
Medium
Topics
premium lock icon
Companies
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def dfs(r, c, k):
            if k == len(word):
                return True
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != word[k]):
                return False
            # To avoid using the same character repeatedly
            tmp = board[r][c]
            board[r][c] = "#"
            res = (dfs(r - 1, c, k + 1) or
                   dfs(r, c + 1, k + 1) or
                   dfs(r + 1, c, k + 1) or
                   dfs(r, c - 1, k + 1))
            # backtrack
            board[r][c] = tmp
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False

solution = Solution()
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")) # True
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")) # True
print(solution.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")) # False

"""
Notes: Though the recursion is tricky, backtracking technique is interesting!
Time Complexity: O(ROWS * COLS * 3^L) where L is len(word)
Space Complexity: O(L), the deepest depth of the recursion is len(word) only
"""