from typing import List
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergesort(nums, left, right):
            if left >= right: return 0
            mid = (left+right)//2
            count = mergesort(nums, left, mid) + mergesort(nums, mid+1, right)
            j = mid+1
            for i in range(left, mid+1):
                while j<=right and nums[j]*2 < nums[i]:
                    j+=1
                count += j-(mid+1)
            merge(nums, left, right, mid)
            return count
 
        def merge(nums, left, right, mid):
            i, j = left, mid+1
            tmp = []
            while i <= mid and j <= right:
                if nums[i]<=nums[j]:
                    tmp.append(nums[i])
                    i+=1
                else:
                    tmp.append(nums[j])
                    j+=1
            while i<=mid:
                tmp.append(nums[i])
                i+=1
            while j<=right:
                tmp.append(nums[j])
                j+=1
            nums[left:right+1] = tmp        
        return mergesort(nums, 0, len(nums)-1)



