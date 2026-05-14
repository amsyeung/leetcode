"""
252. Meeting Rooms
Easy
Topics
Company Tags
Hints
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false
Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
"""

from typing import List

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        curEnd = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < curEnd:
                return False
            curEnd = interval.end
        return True
    
solution = Solution()
l = []
print(solution.canAttendMeetings([])) # True
i = Interval(0, 30)
l.append(i)
i = Interval(5, 10)
l.append(i)
i = Interval(15, 20)
l.append(i)
print(solution.canAttendMeetings(l)) # False
l.clear()
i = Interval(5, 8)
l.append(i)
i = Interval(9, 15)
l.append(i)
print(solution.canAttendMeetings(l)) # True
l.clear()
i = Interval(0, 8)
l.append(i)
i = Interval(8, 10)
l.append(i)
print(solution.canAttendMeetings(l)) # True

"""
Time: O(nlog n), for sorting
Space: O(1)
"""