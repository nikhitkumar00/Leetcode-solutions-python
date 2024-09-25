class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        prefix = defaultdict(int)
        for word in words:
            for i in range(len(word)):
                prefix[word[: i + 1]] += 1

        out = []
        for word in words:
            temp = 0
            for i in range(len(word)):
                temp += prefix[word[: i + 1]]
            out.append(temp)

        return out
