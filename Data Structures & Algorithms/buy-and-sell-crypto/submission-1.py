class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar = prices[0]
        ans =0 
        for i in range(len(prices)):
            minsofar = min(prices[i], minsofar)
            ans = max(ans, prices[i]-minsofar)
        return ans