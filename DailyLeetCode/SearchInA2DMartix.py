# Date: 26-01-2026
#74. Search In a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        low=0
        high=m*n-1
        while low<=high:
            mid=(low+high)//2
            row=mid//n
            col=mid%n
            val=matrix[row][col]
            if val==target:
                return True
            if val<target:
                low=mid+1
            else:
                high=mid-1
        return False