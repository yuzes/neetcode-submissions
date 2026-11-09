class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:        
        def calculateArea(heights: List[int], start: int, end: int) -> int:
            if start > end or start < 0 or end >= len(heights):
                return 0
            minIndex = start
            minHeight = heights[start]
            for i in range(start, end + 1):
                if heights[i] < minHeight:
                    minHeight = heights[i]
                    minIndex = i
            rect = (end - start + 1) * minHeight
            left = calculateArea(heights, start, minIndex - 1)
            right = calculateArea(heights, minIndex + 1, end)
            return max(rect, left, right)

        return calculateArea(heights, 0, len(heights) - 1)