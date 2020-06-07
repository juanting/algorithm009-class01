class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:return []
        self.res = []
        self.helper(nums, n = len(nums),cur= [])
        return self.res
    def helper(self, nums, n, cur):
        if len(cur)== n:
            self.res.append(cur)
        for i in range(len(nums)):
            self.helper(nums[:i]+nums[i+1:], n, cur+[nums[i]])