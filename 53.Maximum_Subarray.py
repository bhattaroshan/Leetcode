class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        m = -float('inf')
        for i in nums:
            s = s+i
            m = max(s,m)
            if s<=0:
                s=0
        return m