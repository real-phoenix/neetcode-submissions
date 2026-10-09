class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        ans = -1
        while(lo<=hi):
            mid = (lo+hi)//2
            # print(lo, mid, hi, ans)
            if nums[mid]<= target:
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
        if ans!=-1 and nums[ans]!=target:
            ans = -1
        return ans