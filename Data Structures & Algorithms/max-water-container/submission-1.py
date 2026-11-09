class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            width = r - l
            if height[l] < height[r]:
                res = max(res, width * height[l])
                l += 1
            else:
                res = max(res, width * height[r])
                r -= 1
        return res