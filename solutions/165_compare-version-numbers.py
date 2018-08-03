"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
"""

class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        dot1 = version1.count('.')
        dot2 = version2.count('.')
        if dot1 > dot2:
            version2 += (dot1 - dot2) * '.0'
        else:
            version1 += (dot2 - dot1) * '.0'
        l1 = version1.split('.')
        l2 = version2.split('.')
        for i, j in zip(l1, l2):
            if int(i) > int(j):
                return 1
            if int(i) < int(j):
                return -1
        return 0