class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Initialize prefix and suffix hash values to zero
        prefix, suffix = 0, 0
        
        # Set a base value for hashing, commonly a prime number to minimize collisions
        base = 29
        
        # Initialize power of the base (used for calculating suffix hash) to 1
        power = 1
        
        # Variable to keep track of the last index where the prefix and suffix hashes match
        last_index = -1
        
        # A large prime number to perform modulus operation and prevent integer overflow
        mod = 10**9 + 7

        # Iterate through the string character by character
        for i, c in enumerate(s):
            # Convert the character to a number (e.g., 'a' -> 1, 'b' -> 2, etc.)
            char = ord(c) - ord("a") + 1
            
            # Update the prefix hash by multiplying the current prefix by the base and adding the character value
            # Apply modulus to keep the value within the bounds of mod
            prefix = (prefix * base + char) % mod
            
            # Update the suffix hash by adding the character value multiplied by the current power
            # Apply modulus to keep the value within bounds of mod
            suffix = (char * power + suffix) % mod
            
            # Update the power for the next character by multiplying by the base and applying modulus
            power = (power * base) % mod

            # Check if prefix and suffix hashes match, indicating a potential palindromic prefix
            if prefix == suffix:
                # Update last_index to the current position as a potential end of the palindromic prefix
                last_index = i

        # Extract the non-palindromic suffix from the string, starting just after the longest palindromic prefix
        suffix_part = s[last_index + 1:]
        
        # Reverse the extracted suffix and prepend it to the original string to form the shortest palindrome
        return suffix_part[::-1] + s