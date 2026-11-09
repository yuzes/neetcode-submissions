class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        curr = []
        def backtrack(i):
            if i >= len(nums):
                res.append(curr.copy())
                return
            # choose to include i
            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()
            # choose to not include i
            backtrack(i + 1)
        backtrack(0)
        return res

    
        