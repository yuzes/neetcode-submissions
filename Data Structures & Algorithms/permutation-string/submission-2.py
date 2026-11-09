class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1arr = self.toArray(s1)
        for i in range(len(s2) - len(s1)+1):
            s2arr = self.toArray(s2[i:i+len(s1)])
            if self.isEqual(s1arr, s2arr):
                return True
        return False
    
    def toArray(self, s: str) -> List[str]:
        res = [0] * 26
        for ch in s:
            res[ord(ch) - ord('a')] += 1
        return res

    def isEqual(self, c1: List[str], c2: List[str]) -> bool:
        for i in range(26):
            if c1[i] != c2[i]:
                return False
        return True