class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parseand(*expr):
            return all(expr)

        def parseor(*expr):
            return any(expr)

        def parsenot(expr):
            return not expr

        s = []
        for c in expression:
            if c == "t":
                s.append("True")
            elif c == "f":
                s.append("False")
            elif c == "&":
                s.append("parseand")
            elif c == "|":
                s.append("parseor")
            elif c == "!":
                s.append("parsenot")
            else:
                s.append(c)

        return eval("".join(s))
