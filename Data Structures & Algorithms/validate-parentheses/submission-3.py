class Solution:
    def isValid(self, s: str) -> bool:
        opens = []
        for parenth in s:
            
            if parenth == ')':
                if not opens or opens.pop() != '(':
                    return False
            elif parenth == ']':
                if not opens or opens.pop() != '[':
                    return False
            elif parenth == '}':
                if not opens or opens.pop() != '{':
                    return False
            else:
                opens += [parenth]
        if not opens:
            return True
        return False
        