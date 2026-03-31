class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        new_str = ""
        for i in range(min(n1,n2)):
            new_str += word1[i]
            new_str += word2[i]

        if n1 > n2:
            new_str += word1[min(n1,n2):]
        if n2 > n1:
            new_str += word2[min(n1,n2):]
        return new_str