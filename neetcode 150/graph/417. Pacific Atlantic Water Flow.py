"""
417. Pacific Atlantic Water Flow
Medium
Topics
premium lock icon
Companies
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

 

Example 1:


Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean 
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean 
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean 
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean 
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean 
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
"""

from typing import List

"""
Time: O((m * n) ^ 2), each cell of either reach_pacific or reach_atlantic tried to travel pacific or atlantic, so boom!
Space: O(m * n)
"""
class Solution: # Time Limited Exceeded
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        result = []
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def reach_pacific(r: int, c: int, path: set) -> bool:
            if r == 0 or c == 0:
                return True
            if (r, c) in path:
                return False
            path.add((r, c))
            h = heights[r][c]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] <= h:
                    if reach_pacific(nr, nc, path):
                        path.remove((r, c))
                        return True
            path.remove((r, c))
            return False

        def reach_atlantic(r: int, c: int, path: set) -> bool:
            if r == ROWS - 1 or c == COLS - 1:
                return True
            if (r, c) in path:
                return False
            path.add((r, c))
            h = heights[r][c]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and heights[nr][nc] <= h:
                    if reach_atlantic(nr, nc, path):
                        path.remove((r, c))
                        return True
            path.remove((r, c))
            return False

        for row in range(ROWS):
            for col in range(COLS):
                if reach_pacific(row, col, set()) and reach_atlantic(row, col, set()):
                    result.append([row, col])
        return result


"""
Time: O(m * n), because each cell has visited twice at most, where one is for pacific dfs and another one is atlantic dfs, only tried one direction at each time (either pacific or atlantic, and then the overlapped cells are the answer)
Space: O(m * n), two set for pacific_reachable + atlantic_reachable + O(m * n) for recursion stack -> O(m * n)
"""
class Solution2:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(r: int, c: int, visited: set) -> None:
            visited.add((r, c))
            h = heights[r][c]
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= h
                ):
                    dfs(nr, nc, visited)

        for c in range(cols):
            dfs(0, c, pacific_reachable)
            dfs(rows - 1, c, atlantic_reachable)

        for r in range(rows):
            dfs(r, 0, pacific_reachable)
            dfs(r, cols - 1, atlantic_reachable)

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])
        return result

solution = Solution2()
print(solution.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])) # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]