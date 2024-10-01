class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rem = defaultdict(int)
        for i in arr:
            rem[(i % k + k) % k] += 1

        for i in arr:
            r = (i % k + k) % k
            if r == 0:
                if rem[0] % 2 != 0:
                    return False
            elif rem[r] != rem[k - r]:
                return False

        return True
