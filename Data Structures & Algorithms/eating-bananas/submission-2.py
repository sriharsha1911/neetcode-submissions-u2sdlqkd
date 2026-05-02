class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=r
        while l<=r:
            k=(l+r)//2
            tot=0
            for i in range(0,len(piles)):
                tot=tot+math.ceil(piles[i] /k)
            if tot>h:
                l=k+1
            elif tot<=h:
                res=min(res,k)
                r=k-1
        return res