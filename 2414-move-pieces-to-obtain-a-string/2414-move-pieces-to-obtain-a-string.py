class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_", "") != target.replace("_", ""):
            return False

        sl_pos = (i for i in range(len(start)) if start[i] == "L")
        sr_pos = (i for i in range(len(start)) if start[i] == "R")
        tl_pos = (i for i in range(len(target)) if target[i] == "L")
        tr_pos = (i for i in range(len(target)) if target[i] == "R")

        for s, t in zip(sl_pos, tl_pos):
            if s < t:
                return False
        for s, t in zip(sr_pos, tr_pos):
            if s > t:
                return False
        return True
