class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open_mapping = { ")" : "(", "]" : "[", "}" : "{" }

        for st in s:
            if st in close_open_mapping:
                if stack and stack[-1] == close_open_mapping[st]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(st)
        return True if not stack else False