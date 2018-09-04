"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0
        
        result  = []
        
        def DFS(grid, x, y, r, c):
            cond = x < 0 or x >= r or y < 0 or y >= c or grid[x][y] == '0'
            if cond:
                return 0
            count = 1
            grid[x][y] = '0'
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                count += DFS(grid, x+i, y+j, r, c)
            return count
        
        r = len(grid)
        c = len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                        result.append(DFS(grid, i, j, r, c))
        return len(result) 