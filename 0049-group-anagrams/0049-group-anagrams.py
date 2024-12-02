class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        out = []
        dic = defaultdict(list)

        for s in strs:
            chars = [0] * 26

            for c in s:
                chars[ord(c) - ord("a")] += 1

            dic[tuple(chars)].append(s)

        for i in dic:
            out.append(dic[i])

        return out
