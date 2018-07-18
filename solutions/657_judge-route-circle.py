"""
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        a = b = 0
        for m in moves:
            if m == 'R':
                a += 1
            elif m == 'L':
                a -= 1
            elif m == 'U':
                b += 1
            elif m == 'D':
                b -= 1
        return [a,b] == [0,0]