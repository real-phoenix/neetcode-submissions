class Solution:
    def twoSum(self, nums: List[int], tar: int) -> List[int]:
        ans = []
        l, r = 0, len(nums)-1
        while(l<r):
            if (nums[l] + nums[r]) == tar:
                ans.append(l+1)
                ans.append(r+1)
                break
            elif (nums[l] + nums[r]) <tar :
                l+=1
            else:
                r-=1
        return ans
