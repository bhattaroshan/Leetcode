from collections import Counter

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        closest = float(inf)
        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1
            while left<right:
                s = nums[i]+nums[left]+nums[right]
                if s==target:
                    return target
                elif s>target:
                    right -= 1
                else:
                    left += 1
                if abs(s-target)<closest:
                    closest = abs(s-target)
                    res = s
        return res