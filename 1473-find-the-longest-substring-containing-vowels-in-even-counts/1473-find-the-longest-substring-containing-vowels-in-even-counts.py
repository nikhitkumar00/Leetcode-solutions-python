class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Map vowels to unique bits in a 5-bit binary representation
        vowel_to_bit = {
            "a": 1,  # 00001 -> bit 0 represents 'a'
            "e": 2,  # 00010 -> bit 1 represents 'e'
            "i": 4,  # 00100 -> bit 2 represents 'i'
            "o": 8,  # 01000 -> bit 3 represents 'o'
            "u": 16, # 10000 -> bit 4 represents 'u'
        }

        # This variable will store the XOR result of the vowels we've encountered so far
        prefix = 0

        # Array to store the first occurrence of each XOR state
        # The array size is 32 because 5 bits can represent 32 different states (2^5 = 32)
        index = [-1] * 32
        
        # Initialize the base case: XOR of 0 is first seen at index 0
        index[0] = 0

        # Variable to store the length of the longest valid substring
        out = 0

        # Traverse through the string `s`
        for i, x in enumerate(s):
            # If the current character is a vowel, update the `prefix` by XORing its bit representation
            if x in vowel_to_bit:
                prefix ^= vowel_to_bit[x]

            # If this XOR state has never been seen before, record its position (1-based index)
            if index[prefix] == -1:
                index[prefix] = i + 1
            else:
                # If this XOR state has been seen before, calculate the length of the substring
                # The substring between the two occurrences of the same XOR state will have
                # even counts of all vowels.
                out = max(out, i - index[prefix] + 1)

        # Return the length of the longest valid substring
        return out