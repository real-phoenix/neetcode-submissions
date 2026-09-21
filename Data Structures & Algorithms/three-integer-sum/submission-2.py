class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(0, len(nums)):
            l, r = 0, len(nums)-1
            val = -1*nums[i]
            while(l<r):
                curSum = nums[l] + nums[r]
                if curSum < val:
                    l+=1
                elif curSum > val:
                    r-=1
                else:
                    if(i==l or i==r):
                        l+=1
                        r-=1
                        continue
                    res = [nums[l], nums[i], nums[r]]
                    l+=1
                    r-=1
                    res.sort()
                    if res not in ans:
                        ans.append(res)
        return ans