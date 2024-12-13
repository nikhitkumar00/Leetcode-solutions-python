class Solution:
    def findScore(self, nums: List[int]) -> int:
        s = set()
        q = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(q)
        score = 0

        while q:
            n, i = heapq.heappop(q)
            if i not in s:
                score += n
                s.add(i)
                s.add(i - 1)
                s.add(i + 1)

        return score
