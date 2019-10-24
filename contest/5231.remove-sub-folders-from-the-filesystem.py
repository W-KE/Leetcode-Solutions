class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(key=lambda x:(x.count("/"), x))
        output = []
        for f in folder:
            sub = False
            for o in output:
                if f.startswith(o + "/"):
                    sub = True
                    break
            if not sub:
                output.append(f)
        return output
