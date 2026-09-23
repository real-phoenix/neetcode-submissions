class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        pref, suf = [0]*(n), [0]*(n)
        pref[0], suf[n-1] = h[0], h[n-1]
        for i in range(1,n):
            pref[i] = max(pref[i-1],h[i])
        for i in range(n-2,-1,-1):
            suf[i] = max(suf[i+1],h[i])
        ans=0
        for i in range(0,n):
            ans+= max(0,min(pref[i], suf[i])-h[i])
        return ans