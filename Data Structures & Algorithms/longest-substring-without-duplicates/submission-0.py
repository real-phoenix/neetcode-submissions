class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, -1
        st = set()
        ans = 0
        while(r<len(s) and l<len(s)):
            while(r+1<len(s) and s[r+1] not in st):
                st.add(s[r+1])
                r+=1
            ans = max(ans, len(st))
            if s[l] in st:
                st.remove(s[l])
                l+=1
            # else:
            #     r = l-1
        return ans