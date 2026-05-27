class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif token == "-":
                a,b = int(stack.pop()), int(stack.pop())
                stack.append(int(b) - int(a))
            elif token == "/":
                a,b = stack.pop(), stack.pop()
                stack.append(int(b / 1))
            else:
                stack.append(int(token))
        return stack[0]