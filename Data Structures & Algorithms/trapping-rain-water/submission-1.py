class Solution:
    def trap(self, height: List[int]) -> int:
        # monotonic decreasing stack, find the next greater height
        stack = [] # store index
        volume = 0
        for i in range(len(height)):
            if not stack or height[i] < height[stack[-1]]:
                stack.append(i)
            else: # stack has elemetn AND height[i] >= stack top -> start pop and calculate volume until we see a higher bar in stack
                while stack and height[i] >= height[stack[-1]]:
                    mid = stack.pop()
                    if stack: # exist left wall
                        left = stack[-1]
                        width = i - left - 1
                        depth = min(height[left], height[i]) - height[mid]
                        volume += width * depth
                stack.append(i)
        return volume