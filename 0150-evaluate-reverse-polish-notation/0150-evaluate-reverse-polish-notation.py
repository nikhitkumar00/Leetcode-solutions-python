class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ("+", "-", "*", "/")
        for x in tokens:
            if x not in operators:
                stack.append(int(x))
            else:
                b = stack.pop()
                a = stack.pop()
                if x == "+":
                    out = a + b
                elif x == "*":
                    out = a * b
                elif x == "-":
                    out = a - b
                else:
                    out = int(a / b)
                stack.append(out)

        return stack[0]