class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i],0) + 1
        count = sorted(count.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            ans.append(count[i][0])
        return ans