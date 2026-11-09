class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair (index, height)
        maxArea = 0
        # consider histogram as mountain
        # this part calculate all possible formed by peak in the middle
        for i, h in enumerate(heights):
            # stack[-1][1] = height of stack top
            # stack top always
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                area = (i - index) * height
                maxArea = max(area, maxArea)
                maxArea = max(maxArea, (i - index + 1) * h)
                start = index
            # extend height[i] to left
            stack.append((start, h))

        # this part calculate base ment
        print(stack)
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
            