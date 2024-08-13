class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        out = []

        candidates.sort()
        # 1, 1, 2, 5, 6, 7, 10

        def backtrack(index, current, value):
            if value == target:
                out.append(current.copy())
                return

            if index == len(candidates) or value > target:
                return

            current.append(candidates[index])
            
            # including the number at index
            backtrack(index + 1, current, value + candidates[index])

            current.pop()

            # not including the number at index
            while (
                index + 1 < len(candidates)
                and candidates[index] == candidates[index + 1]
            ):
                index += 1

            backtrack(index + 1, current, value)

        backtrack(0, [], 0)

        return out
