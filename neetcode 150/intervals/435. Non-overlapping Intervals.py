"""
435. Non-overlapping Intervals
Medium
Topics
premium lock icon
Companies
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
"""

from nt import remove
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        removed = 0
        prev_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start < prev_end: # overlap
                removed += 1
            else:
                prev_end = end
        return removed
        
solution = Solution()
print(solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) # 1, because [1,3] will be removed
print(solution.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]])) # 2, because [1,3] and [3,5] will be removed
print(solution.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]])) # 7

"""
Time: O(nlog n), because sort()
Space: O(1), only removed, prev_end these variables
"""