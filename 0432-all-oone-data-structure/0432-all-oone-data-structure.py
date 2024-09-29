class AllOne:
    def __init__(self):
        self.ds = defaultdict(int)

    def inc(self, key: str) -> None:
        self.ds[key] += 1

    def dec(self, key: str) -> None:
        self.ds[key] -= 1
        if self.ds[key] == 0:
            self.ds.pop(key)

    def getMaxKey(self) -> str:
        if not self.ds:
            return ""

        temp = max(self.ds.values())
        for key in self.ds.keys():
            if self.ds[key] == temp:
                return key

    def getMinKey(self) -> str:
        if not self.ds:
            return ""
            
        temp = min(self.ds.values())
        for key in self.ds.keys():
            if self.ds[key] == temp:
                return key
