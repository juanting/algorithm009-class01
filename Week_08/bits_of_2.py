class Solution:
    def countBits(self, num: int) -> List[int]:
        counts = [0]*(num+1)
        for i in range(1, num+1):
            counts[i] = counts[i&(i-1)]+1   #动态规划
        return counts