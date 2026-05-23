class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref_sz = float('inf')
        for str1 in strs: 
            pref_sz = min(len(str1), pref_sz)
        pref = ""
        for i in range(pref_sz):
            for str1 in strs: 
                if (str1[i] != strs[0][i]):
                    return pref
            pref += strs[0][i]
        return pref 