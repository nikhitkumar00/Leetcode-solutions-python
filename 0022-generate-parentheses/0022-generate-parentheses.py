class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        stack = []

        def backtrack(opened, closeed):
            if opened == n == closeed:
                out.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                backtrack(opened + 1, closeed)
                stack.pop()

            if closeed < opened:
                stack.append(")")
                backtrack(opened, closeed + 1)
                stack.pop()

        backtrack(0, 0)  # opened count, closeed count

        return out
