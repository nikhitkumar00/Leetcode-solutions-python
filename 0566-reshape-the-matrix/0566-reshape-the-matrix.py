class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat

        flat = [j for i in mat for j in i]

        return [flat[row * c : (row + 1) * c] for row in range(r)]
