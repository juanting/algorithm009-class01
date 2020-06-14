class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #贪心算法
        max_arrive = 0
        for i in range(len(nums)-1):
            if i <= max_arrive:  #说明当前位置可以被到达
                max_arrive = max(max_arrive, nums[i]+i)  #更新最大可到达位置
        return max_arrive >= len(nums)-1  #判断是否可以到达最后的位置