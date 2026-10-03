class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens)==1:
            return int(tokens[0])
        idx = 0
        stack = []
        fans = 0
        while(idx<len(tokens)):
            if (tokens[idx] != "*") and (tokens[idx]!="+") and (tokens[idx]!="-") and (tokens[idx]!="/"):
                stack.append(tokens[idx])
                idx+=1
            else:
                num1, num2 = int(stack[-2]), int(stack[-1])
                stack.pop()
                stack.pop()
                ans = 0
                if tokens[idx] == "*":
                    ans = num1*num2
                elif tokens[idx] =="+":
                    ans = num1+num2
                elif tokens[idx] =="-":
                    ans = num1-num2
                else:
                    ans = int(num1/num2)
                idx+=1
                fans = ans
                stack.append(ans)
        return fans
        