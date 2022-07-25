class Solution:
    def cbu(self,n):
        s = 0
        while n:
            if n&1:
                s += 1
            n>>=1
        return s
    
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):    
            res.append(self.cbu(i))
        return res