"""
212. Word Search II
Hard
Topics
premium lock icon
Companies
Hint
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
"""

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = word
        
        ROWS, COLS = len(board), len(board[0])
        res = set()
        
        def dfs(r, c, node):
            char = board[r][c]
            cur_node = node.children[char]
            
            if cur_node.word:
                res.add(cur_node.word)
                cur_node.word = None
            
            board[r][c] = "#"
            
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and
                    board[nr][nc] in cur_node.children):
                    dfs(nr, nc, cur_node)
            board[r][c] = char
            
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)
        return list(res)
    
solution = Solution()
print(solution.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])) # ["eat","oath"]
print(solution.findWords([["a","b"],["c","d"]], ["abcb"])) # []

"""
Time Complexity: O(ROWS * COLS * 3^L) where L is len(word)
Space Complexity: O(N * L), where N is the number of words and L is len(word)
"""
