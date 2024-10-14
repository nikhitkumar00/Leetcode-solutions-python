class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        balloon_count = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        }
        
        return min(count[c] // balloon_count[c] for c in balloon_count)
