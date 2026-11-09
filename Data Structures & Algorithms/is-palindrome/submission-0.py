class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not self.isValid(s[i]):
                i += 1
            while i < j and not self.isValid(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        


        return True
        

    def isValid(self, c):
        return  (ord('A') <= ord(c) and ord('Z') >= ord(c) or
                ord('a') <= ord(c) and ord('z') >= ord(c) or
                ord('0') <= ord(c) and ord('9') >= ord(c))