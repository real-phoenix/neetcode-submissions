class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map1 = defaultdict(list)
        for str1 in strs: 
            key = ''.join(sorted(str1))
            map1[key].append(str1)
        return list(map1.values())
        
