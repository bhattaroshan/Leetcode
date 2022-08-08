class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        index = 0
        res = ""

        while index<length:
            d = 1
            while index-d>=0 and index+d<length and s[index-d]==s[index+d]:
                d += 1
            t = s[index-d+1:index+d]
            if len(t)>len(res):
                res = t

            d=1
            while index-d+1>=0 and index+d<length and s[index-d+1]==s[index+d]:
                d+=1
            t = s[index-d+2:index+d]
            if len(t)>len(res):
                res = t
