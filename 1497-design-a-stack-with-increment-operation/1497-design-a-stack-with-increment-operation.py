class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = [None] * maxSize
        self.top = 0

    def push(self, x: int) -> None:
        if self.top == self.size:
            return
        self.stack[self.top] = x
        self.top += 1

    def pop(self) -> int:
        if self.top == 0:
            return -1
        self.top -= 1
        return self.stack[self.top]

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.top)):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
