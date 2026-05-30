"""
1851. Minimum Interval to Include Each Query
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.

 

Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
Example 2:

Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
"""

import heapq
from typing import List

class Solution: # TLE
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for query in queries:
            min_interval = float('inf')
            for left, right in intervals:
                if left <= query <= right:
                    min_interval = min(min_interval, right - left + 1)
            if min_interval == float('inf'):
                res.append(-1)
            else:
                res.append(min_interval)
        return res

class Solution2:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key=lambda x: x[0])
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        res = [0] * len(queries)
        heap = []
        i = 0
        for idx, q in sorted_queries:
            # Insert
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            # Remove outdated
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            res[idx] = heap[0][0] if heap else -1
        return res
            

solution = Solution2()
print(solution.minInterval([[1,4],[2,4],[3,6],[4,4]], [2,3,4,5])) # [3,3,1,4]
print(solution.minInterval([[2,3],[2,5],[1,8],[20,25]], [2,19,5,22]))  # [2,-1,4,6]

"""
Intuition:
數軸 ─────────────────────────────────────►

intervals 依 left 排好  →  指標 i 跟著 q 往右「開門」放 interval 進 heap
queries 依值排好       →  q 往右掃，不會倒退
heap                   →  此刻「可能包含當前 q」的 interval 裡，取最小 size
pop 頂端 right < q     →  這些 interval 在 q 右邊已經結束，不可能再包含更大的 q…
                         （等等，更大的 q 還可能需要更長的 interval）
                         其實是：對「當前這個 q」，right < q 的一定不包含 q


Time: O(n log n + m log m + n log n) = O((n + m) log n)
  - sort intervals: O(n log n)
  - sort queries: O(m log m)
  - each interval pushed/popped at most once: O(n log n) heap ops total
  - m queries, O(1) answer each
Space: O(n + m)
  - heap up to O(n), res + sorted_queries O(m)
"""