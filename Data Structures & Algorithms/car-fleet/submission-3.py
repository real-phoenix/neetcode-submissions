class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        pair = []
        for i in range(len(pos)):
            pair.append([pos[i],speed[i]])
        pair.sort(reverse=True)
        stack = []
        for cur in pair:
            val = (target-cur[0])/cur[1]
            # print(val)
            if len(stack)==0:
                stack.append(val)
            else:
                if stack[-1]<val:
                    stack.append(val)
        return len(stack)