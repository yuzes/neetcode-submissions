class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        currmin = float('inf')
        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]
            currmin = min(currmin, val)
            if val > nums[r]:
                l = mid + 1
            else: 
                r = mid - 1
        return min(currmin, nums[r])
        