class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}
        for c in tokens:
            # is digit
            if c not in operators:
                stack.append(int(c))
            else:
                a, b = stack.pop(), stack.pop()
                if c == '+':
                    stack.append(a + b)
                if c == '-':
                    stack.append(b - a)
                if c == '*':
                    stack.append(a * b)
                if c == '/':
                    stack.append(int(b / a))
        return stack[-1]