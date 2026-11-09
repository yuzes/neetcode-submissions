class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(i, state):
            if i >= len(nums):
                res.append(state.copy())
                return
            state.append(nums[i])
            backtrack(i+1, state)
            state.pop()

            while(i + 1 < len(nums) and nums[i + 1] == nums[i]):
                i += 1

            backtrack(i + 1, state)
        backtrack(0, [])
        return res
