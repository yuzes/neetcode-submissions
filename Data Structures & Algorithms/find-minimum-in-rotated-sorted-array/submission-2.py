class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        currmin = float('inf')
        while l <= r:
            mid = (l + r) // 2
            currmin = min(currmin, nums[mid])
            if nums[mid] < nums[r]: # in right sorted array, go toleft
                r = mid - 1
            else: # in left sorted array
                l = mid + 1
        return min(currmin, nums[r])


