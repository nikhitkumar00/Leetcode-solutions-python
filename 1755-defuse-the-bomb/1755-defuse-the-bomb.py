class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            return [0] * len(code)

        out = [0] * len(code)

        if k > 0:
            start, end = 1, k
        else:
            start, end = k, -1

        window_sum = sum(code[i % len(code)] for i in range(start, end + 1))
        for i in range(len(code)):
            out[i] = window_sum
            window_sum -= code[(i + start) % len(code)]
            window_sum += code[(i + end + 1) % len(code)]

        return out
