"""
621. Task Scheduler
Medium
Topics
premium lock icon
Companies
Hint
You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

Return the minimum number of CPU intervals required to complete all tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two intervals before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th interval, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.
"""

from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [cnt for cnt in count.values()]
        heapq.heapify_max(heap)
        q = deque()
        time = 0
        while heap or q:
            time += 1
            if heap:
                cnt = heapq.heappop_max(heap) - 1
                if cnt != 0:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                cnt_to_release, _ = q.popleft()
                heapq.heappush_max(heap, cnt_to_release)
        return time
    
solution = Solution()
print(solution.leastInterval(["A","A","A","B","B","B"], 2)) # 8
print(solution.leastInterval(["A","C","A","B","D","B"], 1)) # 6
print(solution.leastInterval(["A","A","A", "B","B","B"], 3)) # 10

"""
Time Complexity: O(N) where N is the total number of tasks. The heap size is bounded by the alphabet size (26 chars) -> O(1), O(N) + O(1) = O(N) 
Space Complexity: O(1) for heap and hashmap of count + O(n + 1) because queue only stores n values, when n + 1 reaches, the first one added to the queue must be popped out first.
Notes:
    I hate this question, medium level, orz...
"""