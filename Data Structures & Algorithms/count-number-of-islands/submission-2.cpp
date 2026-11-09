class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int res = 0;
        for(int row = 0; row < m; row++){
            for(int col = 0; col < n; col++){
                if(grid[row][col] == '1'){
                    backtrack(grid, row, col, m, n);
                    res ++;
                }
            }
        }
        return res;
    }

private:
    void backtrack(vector<vector<char>>& grid, int row, int col, int m, int n){
        if(row < 0 || row >= m || col < 0 || col >= n || grid[row][col] == '0'){
            return;
        }
        grid[row][col] = '0';
        backtrack(grid, row - 1, col, m, n);
        backtrack(grid, row + 1, col, m, n);
        backtrack(grid, row, col - 1, m, n);
        backtrack(grid, row, col + 1, m, n);

    }
};
