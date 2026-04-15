class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        oset=set()
        for a in range(0,len(nums)):
            target=nums[a]*-1
            i=a+1
            j=len(nums)-1
            while(i<j):
                if nums[i]+nums[j]==target:
                    oset.add((nums[a],nums[i],nums[j]))
                    i=i+1
                    j=j-1
                elif nums[i]+nums[j]<target:
                    i=i+1
                elif nums[i]+nums[j]>target:
                    j=j-1
        return list(oset)


        