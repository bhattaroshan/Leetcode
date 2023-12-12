class Solution:
    def reverseVowels(self, s: str) -> str:
        words = list(s)
        res = []
        for count,char in enumerate(words):
            if char in 'aeiouAEIOU':
                res.append(count)
        
        last = len(res)-1
        for i in range(len(res)//2):
            words[res[i]],words[res[last-i]]=words[res[last-i]],words[res[i]]

        return ''.join(words)