class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int res = 0;
        for(int row = 0; row < m; row++){
            for(int col = 0; col < n; col++){
                if(grid[row][col] == 1){
                    int area = backtrack(grid, row, col, m, n);
                    res = max(res, area);
                }
            }
        }
        return res;
    }

private:
    int backtrack(vector<vector<int>>& grid, int row, int col, int m, int n){
        if(row < 0 || row >= m || col < 0 || col >= n || grid[row][col] == 0){
            return 0;
        }
        int num = 1;
        grid[row][col] = 0;
        num += backtrack(grid, row - 1, col, m, n);
        num += backtrack(grid, row + 1, col, m, n);
        num += backtrack(grid, row, col - 1, m, n);
        num += backtrack(grid, row, col + 1, m, n);
        return num;
    }
};
