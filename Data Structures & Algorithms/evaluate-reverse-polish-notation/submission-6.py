class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack += [int(stack.pop()) + int(stack.pop())]
            elif token == '-':
                a, b = int(stack.pop()), int(stack.pop())
                stack += [b - a]
            elif token == '*':
                stack += [int(stack.pop()) * int(stack.pop())]
            elif token == '/':
                a, b = int(stack.pop()), int(stack.pop())
                stack += [int(b/a)]
            else:
                stack += [token]
        return int(stack[0])
        