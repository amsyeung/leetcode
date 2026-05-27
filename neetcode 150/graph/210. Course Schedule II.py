"""
210. Course Schedule II
Medium
Topics
premium lock icon
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
"""

from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            prereq[a].append(b)
        res = []
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
            res.append(course)
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return []
        return res
         
    
solution = Solution()
print(solution.findOrder(2, [[1,0]])) # [0,1]
print(solution.findOrder(4, [[1,0],[2,0],[3,1],[3,2]])) # [0,1,2,3]
print(solution.findOrder(1, [])) # [0]

"""
Time: O(V + E), where V is vertices and E is edges
Space: Space: O(V + E), due to adjacency list + recursion stack + state + output
"""