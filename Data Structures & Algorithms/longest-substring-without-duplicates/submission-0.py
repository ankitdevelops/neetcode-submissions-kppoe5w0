class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left = 0
        max_length = 0

        for end in range(len(s)):
            while s[end] in charset:
                charset.remove(s[left])
                left +=1
            charset.add(s[end])
            max_length = max(max_length,end -left + 1)
        return max_length