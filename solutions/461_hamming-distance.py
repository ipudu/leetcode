"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        result = 0
        lx = [int(i) for i in '{:b}'.format(x)][::-1]
        ly = [int(i) for i in '{:b}'.format(y)][::-1]
        if len(lx) > len(ly):
            for i in range(len(ly)):
                result += abs(lx[i] - ly[i])
            result += sum(lx[len(ly):])
        else:
            for i in range(len(lx)):
                result += abs(lx[i] - ly[i])
            result += sum(ly[len(lx):])
        return result