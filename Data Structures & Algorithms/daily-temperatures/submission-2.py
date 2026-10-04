class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        idx = len(temp)-1
        ans = []
        while(idx>=0):
            if len(stack)==0:
                stack.append(idx)
            else:
                while(len(stack) and temp[idx]>=temp[stack[-1]]):
                    stack.pop()
                if len(stack)==0:
                    ans.append(0)
                    stack.append(idx)
                    idx-=1
                else:
                    ans.append(stack[-1]-idx)
                    stack.append(idx)
                    idx-=1
        return ans[::-1]