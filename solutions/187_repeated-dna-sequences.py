"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""

class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        
        count = 0
        
        while count <= len(s) - 10:
            if s[count:count+10] in d.keys():
                d[s[count:count+10]] += 1
            else:
                d[s[count:count+10]] = 1
            count += 1
        
        result = []
        for key, value in d.items():
            if value > 1:
                result.append(key)
        return result