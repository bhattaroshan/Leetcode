class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x<0:
            sign = -1
        x = abs(x)    
        res = 0
        while x>0:
            res = res*10+(x%10)
            x = x//10
        
        if sign==-1 and res>=pow(2,31):
            return 0
        
        if sign==1 and res>=pow(2,31)-1:
            return 0
        
        return sign*res