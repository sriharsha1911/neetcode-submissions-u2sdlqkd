class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        prev=-1
        cnt=0
        for pos, spd in pairs:
            if prev>0 and prev< (target - pos) / spd :
                prev=(target - pos) / spd
                cnt=cnt+1
            else:
                if prev==-1:
                    prev=(target - pos) / spd
                    cnt=cnt+1
                
        return cnt







        