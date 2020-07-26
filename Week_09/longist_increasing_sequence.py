class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        if not nums: return 0
        max_ = 1
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j]< nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
            max_ = max(dp[i], max_)
        return max_        
        '''
        #二分查找
        if not nums: return 0
        m, res = len(nums), []
        for i in range(m):
            if i==0 or res[-1]< nums[i]:
                res.append(nums[i])
            else:
                l, r, loc = 0, len(res)-1, 0
                while l <= r:
                    mid = (l+r)>>1
                    if nums[i] <= res[mid]:
                        loc = mid
                        r = mid-1
                    else:
                        l = mid+1
                res[loc] = nums[i]   #覆盖掉比它大的元素中最小的那个
        return len(res)