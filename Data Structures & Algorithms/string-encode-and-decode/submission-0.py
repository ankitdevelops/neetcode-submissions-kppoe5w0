class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes = []
        res = ""

        for s in strs:
            sizes.append(str(len(s)))
        for s in sizes:
            res += s
            res += ","
        res += "#"
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sizes = []
        res = []
        i = 0
        
        while s[i] != "#":
            cur = ""
            while s[i] != ",":
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1

        for size in sizes:
            res.append(s[i:i+size])
            i += size
        return res