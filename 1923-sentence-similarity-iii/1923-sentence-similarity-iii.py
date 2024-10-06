class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        s1, s2 = sentence1.split(" "), sentence2.split(" ")
        minlen = min(len(s1), len(s2))

        start, end = 0, 0
        while start < minlen and s1[start] == s2[start]:
            start += 1

        while minlen - end > start and s1[-(end + 1)] == s2[-(end + 1)]:
            end += 1

        return start + end == minlen
