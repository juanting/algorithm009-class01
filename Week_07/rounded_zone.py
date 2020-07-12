class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        if not board: return board
        # 初始化并查集
        m, n = len(board), len(board[0])
        p = [i for i in range(m*n+1)]
        #查找父节点
        def find(x):
            root = x
            while p[root] != root:
                root = p[root]
            while p[x] != x:
                x, p[x] = p[x], root
            return root
        def union(x, y):
            p[find(x)] = find(y)
        
        #遍历，将与边界连通的0合并，其他的不与边界连通的合并
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i==0 or j==0 or i==m-1 or j == n-1:
                        union(i*n+j, m*n)  #边界的都相连
                    else:
                        for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                            nx, ny = i+dx, j+dy
                            if board[nx][ny] == 'O':
                                union(i*n+j, nx*n+ny)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if find(m*n) == find(i*n+j):
                        board[i][j] = 'O'
                    else:
                        board[i][j] = 'X'
        '''
        #dfs
        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        def dfs(x, y):
            board[x][y] = "B"
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and board[nx][ny] =='O':
                    dfs(nx, ny)
        for i in range(m):
            if board[i][0]=='O':
                dfs(i, 0)
            if board[i][n-1]=='O':
                dfs(i, n-1)
        for j in range(n):
            if board[0][j]=='O':
                dfs(0, j)
            if board[m-1][j]=='O':
                dfs(m-1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j] =='O':
                    board[i][j] = 'X'
                elif board[i][j] =='B':
                    board[i][j] = 'O'
