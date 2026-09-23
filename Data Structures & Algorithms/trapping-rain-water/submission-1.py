class Solution:
    def trap(self, h: List[int]) -> int:
        l, r = 0, len(h)-1
        lmax, rmax = h[l], h[r]
        ans = 0
        while(l<r):
            if h[l] <= h[r]:
                l+=1
                lmax = max(lmax, h[l])
                ans += max(0, lmax-h[l])
            else:
                r-=1
                rmax = max(rmax, h[r])
                ans += max(0, rmax-h[r])
                
        return ans