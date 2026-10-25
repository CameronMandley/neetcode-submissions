class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack += [c]
            elif len(stack) == 0:
                return False
            elif c == ')' and stack.pop() != '(':
                return False
            elif c == ']' and stack.pop() != '[':
                return False
            elif c == '}' and stack.pop() != '{':
                return False
        if len(stack) != 0:
            return False
        else:
            return True
        