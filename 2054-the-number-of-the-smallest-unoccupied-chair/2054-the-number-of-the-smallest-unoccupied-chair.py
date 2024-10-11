class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        indexes = [i for i in range(len(times))]
        indexes.sort(key=lambda i: times[i][0])

        used = []  # (leave time, chair number)
        avail = [i for i in range(len(times))]

        for i in indexes:
            arrival, leave = times[i]

            while used and used[0][0] <= arrival:
                leave_time, chair = heapq.heappop(used)
                heapq.heappush(avail, chair)

            chair = heapq.heappop(avail)
            heapq.heappush(used, (leave, chair))

            if i == targetFriend:
                return chair
