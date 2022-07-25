class Solution:
    def get_innermost_letter(self,s):
        open_index = 0
        close_index = 0
        number_index = 0
        index = 0
        length = len(s)
        rep = 1
        while index<length:
            if s[index] == '[':
                open_index = index
                temp = open_index - 1
                while temp>=0 and s[temp].isnumeric():
                    number_index = temp
                    temp -= 1
                rep = int(s[number_index:open_index])
                    
            if s[index] == ']':
                close_index = index
                break
            index += 1
        
        res = s[open_index+1:close_index]        
        f = s[:temp+1]+rep*res+s[close_index+1:]
        return f
         
    def decodeString(self, s: str) -> str: #3[a2[c]]
        while '[' in s:
            s=self.get_innermost_letter(s)
        return s