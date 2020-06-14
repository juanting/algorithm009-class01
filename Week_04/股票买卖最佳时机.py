class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        #贪心算法
        res = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1]> 0:
                res += prices[i]- prices[i-1]
        return max(res, 0)
        '''
        #dp
        res = 0
        dp  = [[0 for _ in range(2)] for _ in range(2)]
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, len(prices)):
            x, y = i%2, (i-1)%2
            dp[x][0] = max(dp[y][0], dp[y][1]+ prices[i])
            dp[x][1] = max(dp[y][1], dp[y][0]-prices[i])
        return dp[(len(prices)-1)%2][0]