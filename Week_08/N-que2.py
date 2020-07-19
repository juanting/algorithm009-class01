class Solution:
    def totalNQueens(self, n: int) -> int:
        if n<=0:
            return 0
        self.count = 0
        self._dfs(n, 0, 0, 0, 0)
        return self.count
    def _dfs(self, n, row, col, pie, na):
        # 终止条件
        if row >= n:
            self.count += 1
            return
        # 得到当前层的空位, 利用n个1来滤除超出n位的bits,位运算的优先级低于加减乘除
        bits = (~(col|pie|na))& (1<<n)-1
        # 依次枚举
        while bits>0:
            # 取出最低位的1放置Q
            P = bits & (-bits)
            # 向下沉
            self._dfs(n, row+1, col|P, (pie|P)<<1, (na|P)>>1)
            # 更新以枚举下一位置
            bits = bits&(bits-1)