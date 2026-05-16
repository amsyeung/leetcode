"""
There is a foreign language which uses the latin alphabet, but the order among letters is not "a", "b", "c" ... "z" as in English.

You receive a list of non-empty strings words from the dictionary, where the words are sorted lexicographically based on the rules of this new language.

Derive the order of letters in this language. If the order is invalid, return an empty string. If there are multiple valid order of letters, return any of them.

A string a is lexicographically smaller than a string b if either of the following is true:

The first letter where they differ is smaller in a than in b.
a is a prefix of b and a.length < b.length.
Example 1:

Input: ["z","o"]

Output: "zo"
Explanation:
From "z" and "o", we know 'z' < 'o', so return "zo".

Example 2:

Input: ["hrn","hrf","er","enn","rfnn"]

Output: "hernf"
"""

from typing import List
from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        in_degree = {}
        for word in words:
            for c in word:
                if c not in adj:
                    adj[c] = set()
                    in_degree[c] = 0
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            if len(w1) > len(w2) and w1.startswith(w2): # check invalid case, i.e. w1=apple, w2=app
                return ""
            min_len = min(len(w1), len(w2))
            for k in range(min_len):
                c1, c2 = w1[k], w2[k]
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degree[c2] += 1
                    break
                
        q = deque()
        
        for c in in_degree:
            if in_degree[c] == 0:
                q.append(c)
        
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            
            for nei in adj[cur]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    q.append(nei)
            
        if len(res) != len(in_degree):
            return ""
        
        return "".join(res)
        
solution = Solution()
print(solution.foreignDictionary(["z","o"])) # "zo"
print(solution.foreignDictionary(["hrn","hrf","er","enn","rfnn"])) # "hernf"

"""
Time: O(M*N)
M = number of words, N = average length of each word
We traverse all characters to build graph and run BFS topological sort.

Space: O(1)
Only 26 lowercase letters at most, adjacency list & in-degree table are constant space.
"""