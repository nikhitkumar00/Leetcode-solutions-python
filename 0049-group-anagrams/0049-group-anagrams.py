class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        out = []
        dic = defaultdict(list)

        for s in strs:
            dic["".join(sorted(s))].append(s)

        for i in dic:
            out.append(dic[i])

        return out
