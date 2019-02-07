#O(n^2)

def is_unique(s):
    """A method to check if a string s has all unique characters"""
    l = len(s)
    for i in range(0, l-1):
        for j in range(i+1, l):
            if s[i] == s[j]:
                return False
    return True