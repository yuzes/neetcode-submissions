class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        

        rows, cols = len(grid), len(grid[0])
        island = 0

        def dfs(grid, row, col):
            if (
                row not in range(rows)
                or col not in range(cols)
                or grid[row][col] == '0'
            ):
                return
            grid[row][col] = '0'
            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)
            return
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    island += 1
                    dfs(grid, i, j)
        return island