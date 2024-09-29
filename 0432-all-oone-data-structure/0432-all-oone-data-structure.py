from collections import defaultdict

class AllOne:
    def __init__(self):
        self.ds = defaultdict(int)
        self.max_key = ""
        self.min_key = ""

    def inc(self, key: str) -> None:
        self.ds[key] += 1

        # Update max_key
        if self.max_key == "" or self.ds[key] > self.ds[self.max_key]:
            self.max_key = key
        
        # Update min_key if it is empty or the current key is the new minimum
        if self.min_key == "" or self.ds[key] < self.ds[self.min_key]:
            self.min_key = key
        elif self.min_key == key:  # If we're incrementing the current min_key, we need to find the new min_key
            self._recalculate_min_key()

    def dec(self, key: str) -> None:
        if key in self.ds:
            self.ds[key] -= 1
            
            if self.ds[key] == 0:
                self.ds.pop(key)
                # Reset min_key or max_key if they were the key removed
                if key == self.max_key or key == self.min_key:
                    self._recalculate_min_max()
            else:
                # Update max_key and min_key after decrement
                if key == self.max_key or self.ds[key] < self.ds[self.min_key]:
                    self._recalculate_min_max()

    def _recalculate_min_max(self):
        if not self.ds:
            self.max_key = ""
            self.min_key = ""
        else:
            self.max_key = max(self.ds, key=self.ds.get)
            self.min_key = min(self.ds, key=self.ds.get)

    def _recalculate_min_key(self):
        # Find the key with the minimum value if the current min_key changes
        if self.ds:
            self.min_key = min(self.ds, key=self.ds.get)
        else:
            self.min_key = ""

    def getMaxKey(self) -> str:
        return self.max_key if self.max_key else ""

    def getMinKey(self) -> str:
        return self.min_key if self.min_key else ""
