from typing import List

class Solution:
    def safe(self,grid,row,col,i,j):
        return i>=0 and i<row and j>=0 and j<col and grid[i][j]=="1"

    def traverse(self,grid,i,j):
        rl = len(grid)
        cl = len(grid[0])
        km = [(-1,0),(0,1),(1,0),(0,-1)]

        queue = []
        queue.append((i,j))
        grid[i][j] = "2"

        while len(queue)>0:
            coord = queue.pop()
            for k in range(4):
                new_coord_x = coord[0]+km[k][0]
                new_coord_y = coord[1]+km[k][1]
                if self.safe(grid,rl,cl,new_coord_x,new_coord_y):
                    grid[new_coord_x][new_coord_y] = "2"
                    queue.append((new_coord_x,new_coord_y))
        
        


    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i,row in enumerate(grid):
            for j,col in enumerate(row):
                if col=="1":
                    self.traverse(grid,i,j)
                    islands += 1
        
        return islands