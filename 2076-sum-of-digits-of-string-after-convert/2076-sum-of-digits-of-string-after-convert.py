class Solution:
    def getLucky(self, s: str, k: int) -> int:
        out = sum(int(digit) for char in s for digit in str(int(ord(char) - 96)))

        for _ in range(k - 1):
            out = sum(int(digit) for digit in str(out))

        return out
