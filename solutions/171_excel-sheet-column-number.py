"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
"""

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_r = s[::-1]
        
        d = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 
             'F': 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10, 
             'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15,
             'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20,
             'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26}
        result = 0
        for i in range(len(s_r)):
            result += d[s_r[i]] * 26 ** i
            
        return result