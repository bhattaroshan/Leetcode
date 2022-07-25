class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        res_r = -1
        res_l = -1
        i = 0
        while i<l and nums[i]!=target:
            i += 1
        
        if i<l:
            res_l = i
        
        while(i<l and nums[i]==target):
            res_r = i
            i += 1
        
        
        return res_l,res_r