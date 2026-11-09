class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in mp:
                return [mp[comp], i]
            mp[n] = i
        return [-1,-1]
        