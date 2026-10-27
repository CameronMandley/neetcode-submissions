class Solution:
    def isValid(self, s: str) -> bool:
        braces = []
        if not s:
            return True
        elif len(s) == 1:
            return False
        for brace in s:
            if brace == ")":
                if len(braces) == 0:
                    return False
                prev_brace = braces.pop()
                if prev_brace != "(":
                    return False
            elif brace == "}":
                if len(braces) == 0:
                    return False
                prev_brace = braces.pop()
                if prev_brace != "{":
                    return False
            elif brace == "]":
                if len(braces) == 0:
                    return False
                prev_brace = braces.pop()
                if prev_brace != "[":
                    return False
            else:
                braces.append(brace)
        return len(braces) == 0
