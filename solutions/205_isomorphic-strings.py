"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""

class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def build(string):
            d = {}
            for i, n in enumerate(string):
                if n in d:
                    d[n].append(i)
                else:
                    d[n] = [i]
            return d
        d1 = build(s)
        d2 = build(t)
        
        for k1 in d1:
            flag = False
            for k2 in d2:
                if d2[k2] == d1[k1]:
                    flag = True
            if not flag:
                return False
        return True