"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""

class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        result = [-1 for i in range(len(S))]
        pos = []
        for i in range(len(S)):
            if C == S[i]:
                pos.append(i)
                result[i] == 0
        
        for i in range(len(result)):
            if result[i] != 0:
                dis = 10000
                for j in pos:
                    if i - j < 0:
                        tmp = -(i-j)
                    else:
                        tmp = i-j
                    if tmp < dis:
                        dis = tmp
                result[i] = dis
        
        return result