class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = False
        late = 0
        for i in s:
            if absent and i == "A":
                return False
            if i == "A":
                absent = True
            if i == "L":
                late += 1
            else:
                late = 0
            if late > 2:
                return False
        return True
