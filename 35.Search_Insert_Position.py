class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index,num in enumerate(nums):
            if num==target:
                return index
            if num>=target:
                break
        if target > nums[index]:
            return index+1
        if target<= nums[index]:
            return index;
           