class Solution:
    # convert to set
    # for each element, check whether it's the start of a seq
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longestSeq = 0
        for n in nums_set:
            # not the start of a seq
            if n - 1 in nums_set:
                continue
            else:
                current = n
                seqLength = 1
                while current + 1 in nums_set:
                    seqLength += 1
                    current += 1
                longestSeq = max(longestSeq, seqLength)
        return longestSeq