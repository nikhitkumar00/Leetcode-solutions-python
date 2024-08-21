class Solution:
    def strangePrinter(self, s: str) -> int:
        # Get the length of the input string
        n = len(s)
        
        # Create a 2D DP array initialized to -1 for memoization
        dp = [[-1] * n for _ in range(n)]
        
        # Start solving the problem for the entire string (from 0 to n-1)
        return self._minPrintTurns(0, n - 1, s, dp)

    def _minPrintTurns(self, start: int, end: int, s: str, dp: list) -> int:
        # Base case: if the substring is empty, no turns are needed
        if start > end:
            return 0

        # If the result is already computed, return it to avoid recomputation
        if dp[start][end] != -1:
            return dp[start][end]

        # Initialize with the case of printing the first character then the rest
        min_turns = 1 + self._minPrintTurns(start + 1, end, s, dp)
        
        # Try to reduce the number of turns by checking for the same character later in the substring
        for k in range(start + 1, end + 1):
            if s[k] == s[start]:
                # Compute the number of turns by splitting the string into two parts
                turns_if_split = self._minPrintTurns(start, k - 1, s, dp) + self._minPrintTurns(k + 1, end, s, dp)
                
                # Update the minimum turns required
                min_turns = min(min_turns, turns_if_split)
        
        # Memoize the result for this substring
        dp[start][end] = min_turns
        
        # Return the computed minimum turns
        return min_turns
