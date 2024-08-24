class Solution:
    def nearestPalindromic(self, n: str) -> str:
        # Handle single-digit numbers
        if len(n) == 1:
            return str(int(n) - 1)

        # Handle numbers like "999"
        if set(n) == {"9"}:
            return str(10 ** len(n) + 1)

        candidates = []
        half = n[: (len(n) + 1) // 2]  # First half of the number

        # Handle edge cases like "1000"
        candidates.append("9" * (len(n) - 1))
        candidates.append(str(10 ** len(n) + 1))

        # Generate palindrome candidates by mirroring the first half
        if len(n) % 2 == 0:
            candidates.append(half + half[::-1])
            candidates.append(str(int(half) - 1) + str(int(half) - 1)[::-1])
            candidates.append(str(int(half) + 1) + str(int(half) + 1)[::-1])
        else:
            candidates.append(half + half[-2::-1])
            candidates.append(str(int(half) - 1) + str(int(half) - 1)[-2::-1])
            candidates.append(str(int(half) + 1) + str(int(half) + 1)[-2::-1])

        # Exclude the original number
        candidates = [x for x in candidates if x != n]

        # Return the closest palindrome
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
