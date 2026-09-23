class Solution:
    def maxProfit(self, price: List[int]) -> int:
        ans = 0
        for i in range(0, len(price)):
            for j in range(i+1, len(price)):
                ans = max(ans, price[j]-price[i])
        return ans