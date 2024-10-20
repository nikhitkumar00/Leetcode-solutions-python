class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parseand(*expr):
            return all(expr)

        def parseor(*expr):
            return any(expr)

        def parsenot(expr):
            return not expr

        return eval(
            expression.replace("t", "True")
            .replace("f", "False")
            .replace("&", "parseand")
            .replace("|", "parseor")
            .replace("!", "parsenot")
        )
