class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        lo, hi = 0, len(nums)-1
        while(lo<=hi):
            mid = (lo+hi)//2
            # print(lo, mid, hi)
            if nums[mid] > nums[hi]:
                if target <= nums[mid] and target>= nums[lo] :
                    ans = mid
                    hi = mid-1
                else:
                    lo = mid+1
            else:
                if target >= nums[mid] and target<= nums[hi]:
                    ans = mid
                    lo = mid+1
                else:
                    hi = mid-1
        if ans!=-1 and nums[ans]!=target:
            ans = -1
        return ans
