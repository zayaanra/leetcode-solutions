class Solution:
    def isValid(self, s: str) -> bool:
        # time complexity - O(n)
        # space complexity - O(n)

        symbols = {")": "(", "}": "{", "]": "["}
        stack = []

        for symbol in s:
            if symbol not in symbols:
                stack.append(symbol)
            else:
                top = len(stack)-1
                if top == -1:
                    return False
                if stack[top] != symbols[symbol]:
                    return False
                stack.pop()

        return len(stack) == 0