class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        # s_count = {}
        # t_count = {}

        # for i in range(len(s)):
        #     s_count[s[i]] = 1 + s_count.get(s[i],0)
        #     t_count[t[i]] = 1 + t_count.get(t[i],0)
        # return s_count == t_count

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for val in count:
            if val != 0:
                return False
        return True