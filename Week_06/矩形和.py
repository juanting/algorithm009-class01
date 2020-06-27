class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        if not mat or not mat[0] or K < 0:
            return [[]]
        n, m = len(mat), len(mat[0])
        # 求二维矩阵presum
        presum = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                presum[i][j] = presum[i - 1][j] + presum[i][j - 1] + mat[i - 1][j - 1] - presum[i - 1][j - 1]

        res = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                lx, ly, rx, ry = max(0, i - K), max(0, j - K), min(n - 1, i + K), min(m - 1, j + K)
                res[i][j] = presum[rx + 1][ry + 1] - presum[rx + 1][ly] - presum[lx][ry + 1] + presum[lx][ly]
        return res