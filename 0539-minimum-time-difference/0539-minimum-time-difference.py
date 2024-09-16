class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for index, time in enumerate(timePoints):
            hour, minute = map(int, time.split(":"))
            timePoints[index] = hour * 60 + minute
        
        timePoints.sort()

        res = 1440 - timePoints[-1] + timePoints[0]

        for i in range(1, len(timePoints)):
            diff = timePoints[i] - timePoints[i-1]
            res = min(res, diff)
            if res == 0:
                return 0
        
        return res