class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_num = {}
        for i, num in enumerate(nums):
            if target-num in map_num:
                return [map_num[target-num], i]
            map_num[num] = i
        return [None, None]