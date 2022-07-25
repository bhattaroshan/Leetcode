class Solution:
    def min_path(self,grid,r,c,i,j,dp):
        if i>=r or j>=c:
            return float('inf')
        if dp[i][j] is not -1:
            return dp[i][j]
        
        if i==r-1 and j==c-1:
            return grid[i][j]
        
        down = grid[i][j]+self.min_path(grid,r,c,i+1,j,dp)
        right = grid[i][j]+self.min_path(grid,r,c,i,j+1,dp)
        m = min(down,right)
        dp[i][j] = m
        return m
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        dp = [[-1 for _ in range(c)] for _ in range(r)]
        res = self.min_path(grid,r,c,0,0,dp)
        return res
        