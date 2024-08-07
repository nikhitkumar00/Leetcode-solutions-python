class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        ones = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }

        tens = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }

        def to_str(n):
            res = []
            if n >= 100:
                res.append(ones[n // 100] + " Hundred")
                n %= 100

            if n >= 20:
                res.append(tens[n // 10])
                n %= 10

            if n >= 1:
                res.append(ones[n])

            return " ".join(res)

        pos = ["", " Thousand", " Million", " Billion"]
        index = 0
        out = []
        
        while num:
            val = to_str(num % 1000)
            if val:
                out.append(val + pos[index])
            index += 1
            num //= 1000
        
        return " ".join(reversed(out))


