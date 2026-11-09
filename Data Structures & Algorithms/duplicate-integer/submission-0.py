class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        data = {}
        for n in nums:
            if n in data:
                return True
            data[n] = True
        return False