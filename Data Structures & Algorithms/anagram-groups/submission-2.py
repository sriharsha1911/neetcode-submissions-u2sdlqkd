class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited=set()
        fin=[]
        d={}
        for i in range(0,len(strs)):
            a=''.join(sorted(strs[i]))
            lis= d.get(a, []) 
            lis.append(strs[i])
            d[a]=lis
        return list(d.values())

        