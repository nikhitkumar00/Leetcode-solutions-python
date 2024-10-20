class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        for c in expression:
            if c == ")":
                s = set()
                while stack[-1] != "(":
                    s.add(stack.pop())
                stack.pop()
                op = stack.pop()

                stack.append(
                    all(s) if op == "&" else any(s) if op == "|" else not s.pop()
                )

            elif c != ",":
                stack.append(True if c == "t" else False if c == "f" else c)

        return stack[-1]
