class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l  = len(nums)
        left = 0
        right = l-1
        
        while left<right:
            if nums[left]&1==0:
                left += 1
                continue
            if nums[right]&1==1:
                right -= 1
                continue
            nums[left],nums[right] = nums[right],nums[left]
        
        return nums
            