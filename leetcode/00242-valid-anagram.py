class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = [s[i] for i in range(len(s))]
        tlist = [t[i] for i in range(len(t))]
        for i in slist, tlist:
            i.sort()
        if slist == tlist:
            return True
        return False
