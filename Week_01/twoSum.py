class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = set()
        for i, x in enumerate(nums):
            if target-x in num_set:
                return [nums.index(target-x), i]
            num_set.add(x)
        return [None, None]