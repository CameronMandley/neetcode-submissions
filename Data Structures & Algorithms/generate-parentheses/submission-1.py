class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        stack = []
        def backTrack(openN, closedN):
            nonlocal output, stack
            if openN == closedN == n:
                output += ["".join(stack)]
                return
            if openN < n:
                stack += ["("]
                backTrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack += [')']
                backTrack(openN, closedN + 1)
                stack.pop()
        backTrack(0, 0)
        return output
            

        