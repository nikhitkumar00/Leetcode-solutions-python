class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:

        current = 0
        total_waiting = 0

        for i in customers:

            if i[0] > current:
                current += i[0] - current

            current += i[1]            
            total_waiting += current - i[0]

        return total_waiting / len(customers)
