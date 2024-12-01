class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash = set(arr)
        for i in arr:
            if 2 * i in hash:
                if i == 0 and arr.count(0) > 1:
                    return True
                elif i != 0:
                    return True
            if i % 2 == 0 and i / 2 in hash:
                if i == 0 and arr.count(0) > 1:
                    return True
                elif i != 0:
                    return True
        return False
