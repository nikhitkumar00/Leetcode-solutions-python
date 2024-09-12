class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)

        count = 0
        for word in words:
            for alphabet in word:
                if alphabet not in s:
                    break
            else:
                count += 1
        
        return count
