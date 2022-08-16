class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        length = len(strs)
        min_length = min([len(x) for x in strs])
        
        for i in range(min_length):
            correct = True
            comp = strs[0][i]
            for j in range(length):
                if comp!=strs[j][i]:
                    correct = False
                    break
            
            if correct:
                res += strs[0][i]
            else:
                break
            
        return res