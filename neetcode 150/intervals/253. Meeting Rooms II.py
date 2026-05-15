"""
Meeting Rooms II
Medium
Topics
Company Tags
Hints
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of rooms required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is NOT considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
room1: (0,40)
room2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

from collections import deque
from tracemalloc import start
from typing import List
from intervalutil import Interval

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(x.start for x in intervals)
        ends = sorted(x.end for x in intervals)
        
        i = j = cur = max_room = 0

        while i < len(starts):
            if starts[i] < ends[j]:
                cur += 1
                i += 1
            else:
                cur -= 1
                j += 1
            max_room = max(max_room, cur)
        return max_room



solution = Solution()
l = []
l.extend([Interval(0,40),Interval(5,10),Interval(15,20)])
print(solution.minMeetingRooms(l)) # 2

"""
Time: O(nlog n), sorted()
Space: O(n), need two lists store 
"""