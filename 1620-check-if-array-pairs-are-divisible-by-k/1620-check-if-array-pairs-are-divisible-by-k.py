class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem = [0] * k

        for i in arr:
            rem[(i % k + k) % k] += 1

        if rem[0] % 2 != 0:
            return False

        for i in range(1, k // 2 + 1):
            if rem[i] != rem[k - i]:
                return False

        return True
