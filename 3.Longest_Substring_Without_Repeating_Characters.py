class Solution:
    def find_longest(self,s,n):
        res = ""
        for i in range(n,len(s)):
            if s[i] not in res:
                res+=s[i]
            else:
                break
        return res
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        for i in range(len(s)):
            res = self.find_longest(s,i)
            if len(res)>m:
                m = len(res)
        return m