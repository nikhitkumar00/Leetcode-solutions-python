class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        stack = []

        def backtrack(open, close):
            if open == n == close:
                out.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()

            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()

        backtrack(0, 0)  # open count, close count

        return out
