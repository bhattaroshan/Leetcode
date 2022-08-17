class Solution:
    def skip_trail(self,s):
        i = 0
        
        while i<len(s) and s[i]==' ':
            i+=1

        return s[i:]
        
    def myAtoi(self, s: str) -> int:
        s = self.skip_trail(s)
        sign = 1
        if len(s)==0:
            return 0
        
        if s[0]=='-':
            sign = -1
        if s[0]=='-' or s[0]=='+':
            s = s[1:]
        res = 0
        for c in s:
            if ord(c)<ord('0') or ord(c)>ord('9'):
                break
            res = res*10+(ord(c)-ord('0'))
        
        if res>=pow(2,31):
            res = pow(2,31)
            if sign==1:
                res-=1
            
        
        return sign*res