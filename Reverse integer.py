def reverse(self, x: int) -> int:
    s = int(str(abs(x))[::-1])
    if x < 0:
        s *= -1

    return s if -2147483648 <= s <= 2147483647 else 0
