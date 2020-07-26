class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        if not cost: return 0
        n = len(cost)
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2,n):
            dp[i] = min(dp[i-2], dp[i-1])+ cost[i]
        return min(dp[-1],dp[-2])
        '''
        if not cost: return 0
        pre, cur = 0, 0
        for i in range(len(cost)):
            pre, cur = cur, min(pre, cur)+cost[i]
        return min(pre, cur)
