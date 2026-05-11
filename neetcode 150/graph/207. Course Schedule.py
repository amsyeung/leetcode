"""
207. Course Schedule
Medium
Topics
premium lock icon
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
"""

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prereq[a] contains courses that must be completed before course a
        prereq = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            prereq[a].append(b)

        # 0 = unvisited, 1 = visiting (in current recursion stack), 2 = visited
        state = [0] * numCourses

        def has_cycle(course: int) -> bool:
            if state[course] == 1:
                return True
            if state[course] == 2:
                return False

            state[course] = 1
            for pre in prereq[course]:
                if has_cycle(pre):
                    return True
            state[course] = 2
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False
        return True
        
    
solution = Solution()
print(solution.canFinish(2, [[1, 0]])) # True
print(solution.canFinish(2, [[1, 0], [0, 1]])) # False
print(solution.canFinish(2, [])) # True
print(solution.canFinish(5, [[1,4],[2,4],[3,1],[3,2]])) # True
print(solution.canFinish(3, [[2, 1], [1, 0]])) # True

"""
Time: O(V + E), where V is vertices and E is edges
Space: O(V), state + recursion stack
"""