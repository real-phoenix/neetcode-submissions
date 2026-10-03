class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" or len(t)>len(s):
            return ""
        count_t, count_s = {}, {}
        for ch in t:
            count_t[ch] = count_t.get(ch,0)+1
        have, need = 0, len(count_t)
        l = 0
        slen = len(s)+1
        ans = ""
        for r in range(len(s)):
            count_s[s[r]] = count_s.get(s[r],0)+1
            if s[r] in t and count_t.get(s[r],0)==count_s.get(s[r],0):
                have+=1
            while(have==need):
                if slen>r-l+1:
                    slen = r-l+1
                    ans = s[l:r+1]
                count_s[s[l]]-=1
                if s[l] in t and count_s[s[l]]<count_t[s[l]]:
                    have-=1
                l+=1
        return ans
            