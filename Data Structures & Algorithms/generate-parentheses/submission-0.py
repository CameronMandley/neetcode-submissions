class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        output = []

        def backtrack(openN, closedN):
            nonlocal stack, output
            if openN == closedN == n:
                output += ["".join(stack)]
                return
            if openN < n:
                stack += ["("]
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack += [")"]
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return output
        