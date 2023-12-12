class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i = 0
        while i<len(s):
            word = ''
            while i<len(s) and s[i]==' ':
                i += 1
            while i<len(s) and s[i]!=' ':
                word += s[i]
                i += 1
            
            if len(word)>0:
                words.append(word)
        
        return ' '.join(words[::-1])
