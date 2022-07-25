class Solution:
    def binSearch(self,arr,target):
        left = 0
        right = len(arr)-1
        while left<=right:
            mid = (left+right)//2
            if arr[mid]<target:
                left = mid+1
            elif arr[mid]>target:
                right = mid-1
            else:
                return True
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        res = []
        for m in matrix:
            res.extend(m)
        #print(res)
        return self.binSearch(res,target)