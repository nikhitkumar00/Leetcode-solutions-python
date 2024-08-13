class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []

        def backtrack(index, current, value):
            if value == target:
                out.append(current.copy())
                return

            if index == len(candidates) or value > target:
                return

            current.append(candidates[index])
            backtrack(index, current, value + candidates[index])
            current.pop()

            backtrack(index + 1, current, value)
        
        backtrack(0, [], 0)

        return out
