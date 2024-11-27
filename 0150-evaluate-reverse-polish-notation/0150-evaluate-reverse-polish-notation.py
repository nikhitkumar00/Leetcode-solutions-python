class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ("+", "-", "*", "/"):
                b = stack.pop()
                a = stack.pop()
                print(a, i, b)
                stack.append(str(int(eval(a + i + b))))
            else:
                stack.append(i)
        return int(stack[-1])
