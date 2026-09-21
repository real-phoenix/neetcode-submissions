class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        s = s.lower()
        for i in range(0, len(s)):
            if (s[i] <='z') and (s[i] >= 'a'):
                new_str +=s[i]
            elif (s[i]>= '0') and (s[i] <='9'):
                new_str +=s[i]
        flag = (new_str == new_str[::-1])
        return flag
            