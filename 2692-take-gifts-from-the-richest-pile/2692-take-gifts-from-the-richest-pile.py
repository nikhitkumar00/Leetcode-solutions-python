class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            v = -heapq.heappop(gifts)
            heapq.heappush(gifts, -int(v**0.5))
        return -sum(gifts)
