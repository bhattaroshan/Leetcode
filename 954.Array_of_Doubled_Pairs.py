class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        res = {}
        arr = sorted(arr,key=lambda x:abs(x))
        for n in arr:
            res[n] = res.get(n,0)+1
        
        for n in arr:
            if res[n]==0:
                continue
            if 2*n in res and res[2*n]>0:
                res[2*n] -= 1
                res[n] -= 1
            else:
                return False

        return True