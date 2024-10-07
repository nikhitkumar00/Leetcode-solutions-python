class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for i in range(len(s)):
            stack.append(s[i])
            while len(stack) > 1 and (
                (stack[-1] == "B" and stack[-2] == "A")
                or (stack[-1] == "D" and stack[-2] == "C")
            ):
                stack.pop()
                stack.pop()

        return len(stack)
