class Solution
    def search(self, nums List[int], target int) - int
        l, r = 0, len(nums)-1
        while l =r
            mid = (l+r)2
            if nums[mid] == target: return mid
            if nums[l] = nums[mid] # 左边有序
                if nums[l] = target = nums[mid]
                    r = mid -1
                else
                    l = mid+1
            else
                if nums[mid]= target = nums[r] #右边有序
                    l = mid+1
                else
                    r = mid - 1 
        return -1