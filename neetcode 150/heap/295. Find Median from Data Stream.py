"""
295. Find Median from Data Stream
Hard
Topics
premium lock icon
Companies
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
"""

import heapq

class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.small, num)
        lmax = heapq.heappop_max(self.small)
        heapq.heappush(self.large, lmax)
        if (len(self.large) - len(self.small)) > 1:
            rmin = heapq.heappop(self.large)
            heapq.heappush_max(self.small, rmin)
        
    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2 != 0:
            return float(self.large[0])
        else:
            return (self.small[0] + self.large[0]) / 2.0
    
medianFinder = MedianFinder()
medianFinder.addNum(1)    # arr = [1]
medianFinder.addNum(2)    # arr = [1, 2]
print(medianFinder.findMedian()) # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)    # arr[1, 2, 3]
print(medianFinder.findMedian()) # return 2.0

"""
Time Complexity: O(logn) for addNum that every heappush or heappop costs O(logn) + O(1) for findMedian -> O(logn)
Space Complexity: O(n), num will store into small or large heap
"""
