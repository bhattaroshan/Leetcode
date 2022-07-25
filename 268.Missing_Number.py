class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        for index,number in enumerate(nums):
            if number is not index:
                return index
        return index+1