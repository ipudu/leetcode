"""
Given two strings s and t which consist of only lowercase letters.

String t is generated by random shuffling string s and then add one more letter at a random position.

Find the letter that was added in t.

Example:

Input:
s = "abcd"
t = "abcde"

Output:
e

Explanation:
'e' is the letter that was added.
"""

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l1, l2= list(s), list(t)
        l1.sort()
        l2.sort()
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return l2[i]
        return l2[-1]