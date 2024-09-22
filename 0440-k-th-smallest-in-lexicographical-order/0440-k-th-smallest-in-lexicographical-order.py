class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(curr, n):
            steps = 0
            first, last = curr, curr + 1
            while first <= n:
                steps += min(last, n + 1) - first
                first *= 10
                last *= 10
            return steps

        # Initialize the current prefix with 1
        curr = 1
        k -= 1  # We decrement k because we start with 1 already counted

        # Traverse the lexicographical tree
        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                # If there are fewer steps than k, move to the next prefix
                curr += 1
                k -= steps
            else:
                # Move down one level in the tree
                curr *= 10
                k -= 1

        return curr
