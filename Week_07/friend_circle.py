class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int: 
        if not M: return 0
        n = len(M)
        #初始化并查集
        p = [i for i in range(n)]
        #合并并查集
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self._union(p, i, j)
        #查找并查集的集合个数
        return len(set(self._parent(p, i) for i in range(n)))
    
    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p1] = p2
    
    def _parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while i != p[i]: #路径压缩
            x, i, p[x] = i, p[i], root
        return root