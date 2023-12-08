class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        i = 0

        if len(str2)>len(str1):
            str1,str2=str2,str1

        while i<len(str1) and i<len(str2):
            if str1[i]==str2[i]:
                res += str1[i]
            else:
                break
            
            i += 1
        
        if len(res)==0: return ""

        length = len(res)
        
        while length>0:
            new_str1 = ""
            new_str2 = ""

            if len(str1)%len(res[0:length])==0 and len(str2)%len(res[0:length]) ==0:
               
                new_str1 = res[0:length]*int(len(str1)/len(res[0:length]))
                new_str2 = res[0:length]*int(len(str2)/len(res[0:length]))
                
                if str1==new_str1 and str2==new_str2:
                    return res[0:length]

            length -= 1
        
        return ""

        