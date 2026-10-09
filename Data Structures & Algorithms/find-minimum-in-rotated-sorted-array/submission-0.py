class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums)-1
        ans = nums[0]
        while(lo<=hi):
            if nums[lo]<nums[hi]:
                ans = min(ans, nums[lo])
            mid = (lo+hi)//2
            ans = min(ans, nums[mid])
            if nums[mid]>=nums[lo]:
                lo = mid+1
            else:
                hi = mid-1
        return ans