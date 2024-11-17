class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        dq = deque()
        min_length = inf

        for i in range(len(nums) + 1):
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                min_length = min(min_length, i - dq.popleft())

            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()

            dq.append(i)

        return min_length if min_length != inf else -1
