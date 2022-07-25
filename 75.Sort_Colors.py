class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = {}
        
        for n in nums:
            a[n] = a.get(n,0)+1
        
        c = 0
        for i in range(3):
            while i in a and a[i]:
                nums[c] = i
                a[i] -= 1
                c += 1
        
        
        
            
        