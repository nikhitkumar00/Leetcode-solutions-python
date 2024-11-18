class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        temp = code.copy()
        if k == 0:
            return [0] * len(code)

        elif k > 0:
            for num in range(len(code)):
                val = 0
                for i in range(1, k + 1):
                    val += temp[(num + i) % len(code)]
                code[num] = val
            return code

        else:
            for num in range(len(code)):
                val = 0
                for i in range(-1, k - 1, -1):
                    val += temp[(num + i) % len(code)]
                code[num] = val
            return code
