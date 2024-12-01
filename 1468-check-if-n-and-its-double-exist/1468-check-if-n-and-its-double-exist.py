class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash = set()
        for i in arr:
            if 2 * i in hash or (i % 2 == 0 and i // 2 in hash):
                return True
            hash.add(i)
        return False
