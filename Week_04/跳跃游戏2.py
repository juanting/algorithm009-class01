class Solution:
    def jump(self, nums: List[int]) -> int:
        max_arrive, res, end = 0, 0, 0
        for i in range(len(nums)-1):  #注意不到最后一个位置去跳
            max_arrive = max(max_arrive, nums[i]+i)
            if i == end: #在到达上次跳完最远的边界处，更新跳跃数，并且将当前能到达的最远处更新为end
                res +=1
                end = max_arrive
        return res