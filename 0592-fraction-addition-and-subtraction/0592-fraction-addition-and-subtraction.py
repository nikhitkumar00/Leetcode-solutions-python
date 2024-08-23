from fractions import Fraction


class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression += "+"
        numbers = []

        i = 0
        negative = 0
        temp = 0
        while i < len(expression):
            if expression[i] in ("+", "-"):
                if i != 0:
                    denominator = temp
                    temp = 0
                    if negative:
                        numerator *= -1
                        negative = 0
                    numbers.append(Fraction(numerator, denominator))

                negative = expression[i] == "-"
                i += 1
                continue

            if expression[i] == "/":
                numerator = temp
                temp = 0
                i += 1

            temp = temp * 10 + int(expression[i])
            i += 1

        out = str(sum(numbers))
        return out if '/' in out else out + '/1'
