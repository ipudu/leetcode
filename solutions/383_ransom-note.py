"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d1, d2 = {}, {}
        for c in ransomNote:
            if c in d1.keys():
                d1[c] += 1
            else:
                d1[c] = 1
        for c in magazine:
            if c in d2.keys():
                d2[c] += 1
            else:
                d2[c] = 1
        for key in d1:
            if not key in d2.keys():
                return False
            else:
                if d1[key] > d2[key]:
                    return False
        return True