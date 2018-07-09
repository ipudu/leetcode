"""
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
 

Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""

class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        if A == B:
            s = set()
            for a in A:
                if a in s:
                    return True
                else:
                    s.add(a)
            return False

        a = []
        b = []
        result = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                result += 1
                a.append(A[i])
                b.append(B[i])

        
        if result == 2 and a == b[::-1]:
            return True
        else:
            return False