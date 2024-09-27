class MyCalendarTwo:

    def __init__(self):
        self.events = []
        self.overlap_events = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlap_events:
            if start < e and end > s:
                return False

        for s, e in self.events:
            if start < e and end > s:
                self.overlap_events.append((max(s, start), min(end, e)))

        self.events.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
