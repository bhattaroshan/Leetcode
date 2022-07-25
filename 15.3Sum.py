from collections import Counter

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left<right:
                s = nums[i]+nums[left]+nums[right]
                new_arr = [nums[i],nums[left],nums[right]]
                if s==0 and new_arr not in res:
                    res.append(new_arr)
                    left+=1
                    right-=1
                elif s>0:
                    right -= 1
                else:
                    left += 1
        return res
                