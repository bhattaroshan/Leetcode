class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numbers = {}
        for i in nums:
            numbers[i] = True
        
        for i in range(1,len(nums)+2):
            if i not in numbers:
                return i
        return 0
        