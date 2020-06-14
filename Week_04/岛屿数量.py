class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #染色法
        if not grid or len(grid[0])==0: return 0
        self.m, self.n, island= len(grid), len(grid[0]), 0
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        for x in range(self.m):
            for y in range(self.n):
                if grid[x][y] =='1':
                    island +=1
                    self.dfs(grid, x, y)
        return island
    def dfs(self, grid, x, y):
        grid[x][y] = 0 
        for k in range(4):
            new_x, new_y = x+self.dx[k], y+ self.dy[k]
            if 0 <= new_x < self.m and 0<= new_y < self.n and grid[new_x][new_y]=='1':
                self.dfs(grid, new_x, new_y)