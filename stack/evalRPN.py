class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        vals = []
        ans = 0

        if len(tokens) == 1:
            return int(tokens[0])

        while tokens:
            tok = tokens.pop(0)
            if tok == "+":
                x = vals.pop()
                y = vals.pop()
                vals.append(int(x) + int(y))

            elif tok == "-":
                x = vals.pop()
                y = vals.pop()
                vals.append(int(y) - int(x))

            elif tok == "*":
                x = vals.pop()
                y = vals.pop()
                vals.append(int(x) * int(y))

            elif tok == "/":
                x = vals.pop()
                y = vals.pop()
                vals.append(int(int(y) / int(x)))

            else:
                vals.append(tok)

        return vals[0]


# better

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok in "+-*/":
                x = stack.pop()
                y = stack.pop()
                if tok == "+":
                    stack.append(y + x)
                elif tok == "-":
                    stack.append(y - x)
                elif tok == "*":
                    stack.append(y * x)
                else:
                    # Convert to int to simulate integer division
                    stack.append(int(y / x))
            else:
                # Convert to int since operands are integers
                stack.append(int(tok))

        return stack[0]
