class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0': return 0
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1 
        dp[1] = 0 if s[0] =='0' else 1
        for i in range(2, len(s)+1):
            if 0<int(s[i-1])<=9:   #如果当前数字s【i-1】在1-9之间 说明可以加上前一位是1位数编码的个数
                dp[i] += dp[i-1]
            if 10<= int(s[i-2:i]) <=26: 
                #如果当前数字与前一位的数字组成在10-26之间，说明可以加上两位编码的情况
                dp[i] += dp[i-2]
        return dp[-1]