class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        pos = sorted(set(arr))

        dic = {}
        for index, val in enumerate(pos):
            dic[val] = index + 1
        
        return [dic[x] for x in arr]