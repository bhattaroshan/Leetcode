class Solution:
    def safe(self,grid,row,col,r,c):
        return r>=0 and r<row and c>=0 and c<col and grid[r][c]==1
    
    def dfs(self,grid,row,col,r,c,d):
        rm = [-1,0,1,0]
        cm = [0,1,0,-1]
        grid[r][c] = 0
        
        d[0] += 1
        for i in range(4):
            nr = r+rm[i]
            nc = c+cm[i]
            if self.safe(grid,row,col,nr,nc):
                self.dfs(grid,row,col,nr,nc,d)
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        d = [0]
        row = len(grid)
        col = len(grid[0])
        res = 0
        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    self.dfs(grid,row,col,r,c,d)
                    res = max(d[0],res)
                    d[0]=0
                    count += 1
                    
        print(count)
        return res