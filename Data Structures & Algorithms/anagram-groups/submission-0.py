class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ascii = tuple(count)
            if ascii not in ans:
                ans[ascii] = []
            ans[ascii].append(s)
        return ans.values()
        