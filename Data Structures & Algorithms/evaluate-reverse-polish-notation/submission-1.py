class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        # ["4","13","5","/","+"]
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))

            elif token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(a - b)

                elif token == "*":
                    stack.append(a * b)

                elif token == "/":
                    stack.append(int(a / b))
                 

        return stack[-1]