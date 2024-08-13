class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        out = []

        def backtrack(number, current, value):
            if value == n and len(current) == k:
                out.append(current.copy())
                return

            if value > n or number == 10:
                return

            current.append(number)
            backtrack(number + 1, current, value + number)
            current.pop()

            backtrack(number + 1, current, value)

        backtrack(1, [], 0)

        return out
