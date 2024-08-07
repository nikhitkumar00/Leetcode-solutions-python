class Solution:
    def numberToWords(self, num: int) -> str:

        # Base case: return "Zero" if the input number is 0
        if num == 0:
            return "Zero"

        # Define lists for ones and tens place words
        ones = [
            "",  # 0
            "One",  # 1
            "Two",  # 2
            "Three",  # 3
            "Four",  # 4
            "Five",  # 5
            "Six",  # 6
            "Seven",  # 7
            "Eight",  # 8
            "Nine",  # 9
            "Ten",  # 10
            "Eleven",  # 11
            "Twelve",  # 12
            "Thirteen",  # 13
            "Fourteen",  # 14
            "Fifteen",  # 15
            "Sixteen",  # 16
            "Seventeen",  # 17
            "Eighteen",  # 18
            "Nineteen",  # 19
        ]

        tens = [
            "",  # 0
            "",  # 10
            "Twenty",  # 20
            "Thirty",  # 30
            "Forty",  # 40
            "Fifty",  # 50
            "Sixty",  # 60
            "Seventy",  # 70
            "Eighty",  # 80
            "Ninety",  # 90
        ]

        # Define a list for position words (thousand, million, billion)
        pos = ["", " Thousand", " Million", " Billion"]
        index = 0  # Initialize index for position words
        out = []  # Initialize output list

        # Loop through the number in groups of 3 digits
        while num:
            val = num % 1000  # Get the last 3 digits

            if val:  # If the group is not zero
                res = []  # Initialize a list to store the words for this group

                # Handle hundreds place
                if val >= 100:
                    res.append(ones[val // 100] + " Hundred")
                    val %= 100

                # Handle tens place
                if val >= 20:
                    res.append(tens[val // 10])
                    val %= 10

                # Handle ones place
                if val >= 1:
                    res.append(ones[val])

                # Append the words for this group to the output list
                out.append(" ".join(res) + pos[index])
            
            index += 1  # Move to the next position word
            num //= 1000  # Move to the next group of 3 digits

        # Join the output list into a single string and return
        return " ".join(reversed(out))
