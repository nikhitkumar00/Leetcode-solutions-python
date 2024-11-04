class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""
        
        cur = 1
        out = []
        prev = word[0]

        for i in range(1, len(word)):
            if prev != word[i] or cur == 9:
                out.append(str(cur) + prev)
                prev = word[i]
                cur = 1
            else:
                cur += 1
        
        out.append(str(cur) + prev)

        return "".join(out)
