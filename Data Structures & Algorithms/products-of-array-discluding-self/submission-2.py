class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1, 1, 2, 8
        # 48, 24, 6, 1
        n = len(nums)
        prefix = [0] * n
        suffix = [0] * n
        result = [0] * n
        prefix[0] = suffix[n - 1] = 1
        for i in range(1, n):
            prefix[i] = nums[i - 1] * prefix[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]
        for i in range(0, n):
            result[i] = prefix[i] * suffix[i]
        return result