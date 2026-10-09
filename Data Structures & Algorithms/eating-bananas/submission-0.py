class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(mid: int) -> int:
            ans = 0
            for pile in piles:
                ans += (pile+mid-1)//mid
            return ans<=h
        
        lo, hi = 1, sum(piles)
        ans = -1
        while(lo<=hi):
            mid = (lo+hi)//2
            if check(mid):
                ans = mid
                hi = mid-1
            else:
                lo = mid+1
        return ans 