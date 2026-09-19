class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        st = sorted(st)
        print(st)
        prev = float('-inf')
        ans = []
        res = 0
        for x in st:
            if prev == float('-inf'):
                ans.append(x)
                prev = x
            else:
                if(prev+1 == x):
                    ans.append(x)
                    prev = x
                else:
                    ans = []
                    ans.append(x)
                    prev = x
            res = max(res, len(ans))
            # print(res, len(ans))
        return res