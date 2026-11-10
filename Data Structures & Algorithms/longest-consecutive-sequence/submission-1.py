class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        distinct = set(nums)
        result = 0
        for n in nums:
            if n - 1 not in distinct:
                length = 1
                end = n + 1
                while end in distinct:
                    end += 1
                    length += 1
                result = max(length, result)
        return result

        