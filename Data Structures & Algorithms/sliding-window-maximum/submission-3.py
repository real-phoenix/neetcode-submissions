import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        st = {}
        l, r = 0, 0
        ans = []
        for i in range(k):
            heapq.heappush(max_heap,-nums[r])
            st[nums[r]] = st.get(nums[r],0)+1
            r+=1
        ans.append(-max_heap[0])
        while(r<len(nums)):
            st[nums[l]] = st.get(nums[l],0)-1
            while max_heap and st.get(-max_heap[0], 0) == 0:
                heapq.heappop(max_heap)
            l+=1
            st[nums[r]] = st.get(nums[r],0)+1
            heapq.heappush(max_heap,-nums[r])
            ans.append(-max_heap[0])
            r+=1
        return ans
        