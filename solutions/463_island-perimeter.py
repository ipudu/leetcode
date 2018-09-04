"""

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
"""

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        
        def perimeter(grid, x, y, r, c):
            result = 0
            if grid[x][y] == 1:
                if x - 1 < 0:
                    result += 1
                else:
                    result += 1 - grid[x-1][y]
                if y - 1 < 0:
                    result += 1
                else:
                    result += 1 - grid[x][y-1]
                if x + 1 >= r:
                    result += 1
                else:
                    result += 1 - grid[x+1][y]
                if y + 1 >= c:
                    result += 1
                else:
                    result += 1 - grid[x][y+1]
            return result
        
        r = len(grid)
        c = len(grid[0])
        
        for x in range(r):
            for y in range(c):
                result += perimeter(grid, x, y, r, c)
        return result