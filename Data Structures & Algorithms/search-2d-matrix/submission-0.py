class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        l1=0
        r1=len(matrix[0])-1
        while l<=r:
            mid=(l+r)//2
            if target<matrix[mid][0]:
                r=mid-1
            elif target>=matrix[mid][0] and target<=matrix[mid][r1]:
                while l1<=r1:
                    mid1=(l1+r1)//2
                    if target<matrix[mid][mid1]:
                        r1=mid1-1
                    elif target>matrix[mid][mid1]:
                        l1=mid1+1
                    elif target==matrix[mid][mid1]:
                        return True
            elif target>matrix[mid][0]:
                l=mid+1
        return False
                    

            