"""
51. N-Queens
Hard
Topics
premium lock icon
Companies
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

A queen in a chessboard can attack horizontally, vertically, and diagonally.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
"""

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c

        def dfs(r: int, path: List[str]):
            if r == n:
                res.append(path.copy())
                return
            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
               
                row = "." * c + "Q" + "." * (n - c - 1)
                path.append(row)
                
                dfs(r + 1, path)
                
                path.pop()
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)
        
        dfs(0, [])
        return res
                    
        
    
s = Solution()
print(s.solveNQueens(4)) # [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]