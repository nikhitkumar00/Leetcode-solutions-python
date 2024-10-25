class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        hashset = set(folder)
        out = []
        
        for folder in hashset:
            is_sub = False
            prefix = folder

            while prefix != "":
                pos = prefix.rfind("/")
                if pos == -1:
                    break
                
                prefix = prefix[:pos]

                if prefix in hashset:
                    is_sub = True
                    break
            
            if not is_sub:
                out.append(folder)
        
        return out