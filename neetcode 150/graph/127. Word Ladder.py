"""
127. Word Ladder
Hard
Topics
premium lock icon
Companies
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
"""

from collections import deque
from typing import List
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        q = deque()
        q.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        
        while q:
            for _ in range(len(q)):
                word, steps = q.popleft()
                if word == endWord:
                    return steps
                for i in range(len(word)):
                    for c in string.ascii_lowercase:    
                        new_word = word[0:i] + c + word[i+1:]
                        if new_word in wordSet and new_word not in visited:
                            visited.add(new_word)
                            q.append((new_word, steps + 1))
        return 0
    
solution = Solution()
print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])) # 5
print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"])) # 0

"""
Time: O(N * L * 26), where N = len(wordList), L = word length; each word dequeued once, try 26 letters per position
Space: O(N), wordSet + visited + queue
"""