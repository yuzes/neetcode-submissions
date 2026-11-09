class Solution:
    # use : as seperator
    # format <count> - <:> <strings that 
    def encode(self, strs: List[str]) -> str:
        codes = []
        for s in strs:
            codes.append(str(len(s)))
            codes.append(":")
            codes.append(s)
        return ''.join(codes)


    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i + 1
            while s[j] != ':':
                j += 1
            # s[j] == ':'
            length = int(s[i:j])
            i = j + length + 1
            result.append(s[j+1:i])
        return result