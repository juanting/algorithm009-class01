###  动态规划
#### 1.不同路径和的状态定义
题目一：无障碍路径和
https://leetcode-cn.com/problems/unique-paths/

从左上角到右下角递推：dp为到达改位置的路径和
在二维中递推方程为：
```angular2
dp[i][j] = dp[i][j-1]+ dp[i-1][j]
```

压缩到一维：
```angular2
dp[i] = dp[i-1]+dp[i]
```
题目整体代码为：
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 0 or n<=0: return 0
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                dp[j] = dp[j-1]+ dp[j]
        return dp[-2]
```

题目二：有障碍
仅仅需要在状态定义转换时考虑障碍存在时为0即可
代码:
```
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        if obstacleGrid[0][0] == 1: return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j] if obstacleGrid[i][j]==0 else 0
        return dp[-1][-1]
        '''
        #dp一维
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]==1: return 0
        m ,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        for i in range(m):
            for j in range(n):
                dp[j] =dp[j] + dp[j-1] if obstacleGrid[i][j] == 0  else 0  
                #如果直接+= 等效于不等于0时加0！！!!
        return dp[-2]
```
