class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                stack += [stack.pop() + stack.pop()]
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                stack += [b-a]
            elif c == '*':
                stack += [stack.pop() * stack.pop()]
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                stack += [int(float(b)/a)]
            else:
                stack += [int(c)]
        return int(stack[0])
        