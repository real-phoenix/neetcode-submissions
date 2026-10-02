class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        orig_mp = {}
        for i in range(len(s1)):
            orig_mp[s1[i]] = orig_mp.get(s1[i], 0) + 1
        check_mp = {}
        l, r = 0, -1
        while(l<len(s2)):
            while((r+1)<len(s2) and check_mp.get(s2[r+1], 0) < orig_mp.get(s2[r+1], 0)):
                r+=1
                check_mp[s2[r]] = check_mp.get(s2[r],0)+1
            print(l, r)
            if (check_mp == orig_mp):
                return True
            if s2[l] in check_mp:
                check_mp[s2[l]] -= 1
            if(r<l):
                l+=1
                r = l-1
            else:
                l+=1
        return False