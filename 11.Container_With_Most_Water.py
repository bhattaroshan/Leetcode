class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height) 
        left = 0
        right = length-1
        res = 0
        while(left<right):
            tmp = min(height[left],height[right])*(right-left)
            res = max(tmp,res)
            if height[left]<=height[right]:
                left += 1
            else:
                right -= 1
                
        return res