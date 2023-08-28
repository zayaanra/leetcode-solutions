class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        operators = {"+", "-", "*", "/"}
        stack = []
        for tk in tokens:
            if tk not in operators:
                stack.append(tk)
            else:
                x, y = int(stack.pop()), int(stack.pop())
                if tk == "+":
                    stack.append(x + y)
                elif tk == "*":
                    stack.append(x * y)
                elif tk == "-":
                    stack.append(y - x)
                else:
                    stack.append(int(y/x))
        return stack[0]