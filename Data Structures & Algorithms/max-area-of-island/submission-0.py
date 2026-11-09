class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island = 0

        def dfs(grid, row, col):
            if (
                row not in range(rows)
                or col not in range(cols)
                or grid[row][col] == 0
            ):
                return 0
            area = 1
            grid[row][col] =  0
            area += dfs(grid, row + 1, col)
            area += dfs(grid, row - 1, col)
            area += dfs(grid, row, col + 1)
            area += dfs(grid, row, col - 1)
            return area
        
        maxArea = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(grid, i, j))
        return maxArea