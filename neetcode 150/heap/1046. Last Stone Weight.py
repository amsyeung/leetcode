"""
1046. Last Stone Weight
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

 

Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
Example 2:

Input: stones = [1]
Output: 1
"""

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)
            if y != x:
                heapq.heappush(max_heap, -(y - x))
        return -max_heap[0] if max_heap else 0
    
solution = Solution()
print(solution.lastStoneWeight([2,7,4,1,8,1])) # 1
print(solution.lastStoneWeight([1])) # 1
print(solution.lastStoneWeight([2,2])) # 0

"""
Time Complexity: O(NlogN), where O(N) for heapify and O(logN) for 2 heappop and 1 heappush
Space Complexity: O(n) because all elements push into heap for comparision
"""