class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0 for i in range(len(arr) + 1)]
        for i in range(len(arr)):
            prefix[i + 1] = prefix[i] ^ arr[i]

        out = []
        for l, r in queries:
            out.append(prefix[r + 1] ^ prefix[l])

        return out
