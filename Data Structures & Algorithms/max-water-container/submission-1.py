class Solution:
    def maxArea(self, h: List[int]) -> int:
        l, r = 0, len(h)-1
        ans = 0
        while l<r:
            ans = max(ans, min(h[l], h[r])*(r-l))
            if h[l]>h[r]:
                r-=1
            else: l+=1
        return ans