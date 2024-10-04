class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        out = 0

        for i in range(k):
            out += happiness[i] - i if happiness[i] > i else 0
        
        return out
