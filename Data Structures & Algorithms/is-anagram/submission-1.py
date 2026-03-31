class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lst  = [0] * 26

        for i in range(len(s)):
            lst[ord(s[i]) - ord('a')] += 1
            lst[ord(t[i])- ord('a')] -= 1

        for val in lst:
            if val != 0:
                return False
        return True