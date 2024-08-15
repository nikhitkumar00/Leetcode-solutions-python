class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        return list(set(map(min, matrix)).intersection(set(map(max, zip(*matrix)))))
