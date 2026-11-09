class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
            else:
                if openN < n:
                    stack.append("(")
                    backtrack(openN+1, closeN)
                    stack.pop()
                if closeN < n and closeN < openN:
                    stack.append(")")
                    backtrack(openN, closeN+1)
                    stack.pop()
        backtrack(0, 0)
        return res

            