class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        res = [1]*len(nums)
        for i,n in enumerate(nums):
            res[i] = prod
            prod *= n
        
        prod = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= prod
            prod *= nums[i]
        
        return res