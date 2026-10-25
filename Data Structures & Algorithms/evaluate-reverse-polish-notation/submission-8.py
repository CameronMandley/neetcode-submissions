class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                stack += [stack.pop() + stack.pop()]
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack += [b - a]
            elif token == '*':
                stack += [stack.pop() * stack.pop()]
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                stack += [int(float(b) / a)]
            else:
                stack += [int(token)]
        return int(stack[0])
        