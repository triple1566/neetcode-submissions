class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sarr = list(s)
        tarr = list(t)

        for i in sarr:
            if i in tarr:
                tarr.remove(i)
            else:
                return False
        if (tarr==[]):
            return True
        return False
