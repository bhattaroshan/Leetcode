class Solution:
   
    def __init__(self):
        self.dp = {}
        
    def climbStairs(self, n: int) -> int:
        if n<0:
            return 0
        if n==0:
            return 1
        
        if n in self.dp.keys():
            return self.dp[n]
        
        res = self.climbStairs(n-1)+self.climbStairs(n-2)
        self.dp[n] = res
        return res