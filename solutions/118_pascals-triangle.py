"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = [[1]]
        row = [1]
        for i in range(numRows-1):
            row = [x+y for x, y in zip([0]+row, row+[0])]
            result.append(row)
        return result