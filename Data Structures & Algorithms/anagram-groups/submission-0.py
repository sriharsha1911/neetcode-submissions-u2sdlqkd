class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        visited=set()
        fin=[]
        for i in range(0,len(strs)):
            lis=[]
            if strs[i] in visited:
                continue
            else:
                lis.append(strs[i])
                visited.add(strs[i])
            for j in range(i+1,len(strs)):
                if Counter(strs[i])==Counter(strs[j]):
                    lis.append(strs[j])
                    visited.add(strs[j])
            fin.append(lis)
        return fin