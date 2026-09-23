class Solution:
    def maxArea(self, heights: List[int]) -> int:
        mn = min(heights)
        mx = max(heights)
        # print(mn, mx)
        l, r = 0, len(heights)-1
        ans =0
        for curh in range(mn, mx+1):
            # print(ans, l, r)
            if l<len(heights) and r>=0:
                if heights[l]>=curh and heights[r]>=curh:
                    ans = max(ans, min(heights[l], heights[r])*(r-l))
                elif heights[l]<curh:
                    while(l<r):
                        if heights[l]>=curh:
                            break
                        else:
                            l+=1
                    ans = max(ans, min(heights[l], heights[r])*(r-l))
                else:
                    while(l<r):
                        if heights[r]>=curh:
                            break
                        else:
                            r-=1
                    ans = max(ans, min(heights[l], heights[r])*(r-l))
        return ans

