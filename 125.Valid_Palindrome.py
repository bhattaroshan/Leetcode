class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""
        for t in s:
            if t.isalnum():
                res += t
        length = len(res) 
        left = 0
        right = length-1
        while left<right:
            if res[left]!=res[right]:
                return False
            left += 1
            right -= 1
        return True
            
        