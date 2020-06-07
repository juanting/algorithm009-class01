class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.helper(nums, [])
        return self.res
    def helper(self, nums, cur):
        if not nums:
            if cur[:] not in self.res:
                self.res.append(cur[:])  #浅copy 否则cur会改变res中的结果
            return
        for i in range(len(nums)):
            cur.append(nums[i])
            self.helper(nums[:i]+nums[i+1:], cur)
            cur.pop()