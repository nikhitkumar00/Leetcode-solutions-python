class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        out = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                out.append((arr[i], arr[j]))
        return sorted(out, key=lambda x: x[0] / x[1])[k - 1]
