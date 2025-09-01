class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []
        for char in s:
            if char != "#":
                s1.append(char)
            else:
                if s1:
                    s1.pop()
                else:
                    continue
        for char in t:
            if char != "#":
                s2.append(char)
            else:
                if s2:
                    s2.pop()
                else:
                    continue
        return s1 == s2
