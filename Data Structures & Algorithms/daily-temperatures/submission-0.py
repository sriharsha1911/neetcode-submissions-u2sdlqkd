class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res=[]
        for i  in range(0,len(temperatures)):
            flg=0
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    res.append(j-i)
                    flg=1
                    break
            if flg==0:
                res.append(0)
        return res



        