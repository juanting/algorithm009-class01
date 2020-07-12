from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        f = [i for i in range(m*n)]
        def find(x):
            root = x
            while f[root]!=root:
                root = f[root]
            
            while f[x] != x:
                i = x
                x = f[i]
                f[x] = root
            return root
        def union(x, y):
            f[find(x)] = find(y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    for dx, dy in ([-1, 0], [0, -1]):
                        nx, ny = i+dx, j+dy
                        if 0 <= nx < m and 0<= ny <n and grid[nx][ny]=="1":
                            union(i*n+j, nx*n+ny)
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    res.add(find(i*n+j))
        return len(res)
print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))             
                    