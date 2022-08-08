class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append((i,nums[i]))
            
        res = sorted(res,key=lambda item:item[1])
        
        left = 0
        right = len(res)-1
        for i in range(len(res)):
            s = res[left][1]+res[right][1]
            if s<target:
                left += 1
            elif s>target:
                right -= 1
            else:
                return [res[left][0],res[right][0]]
            
        
        return [0,0]
        