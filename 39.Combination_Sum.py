class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        queue = [[]]
        count = 0
        res = []
        while queue:
            current_num = queue.pop()
            s = sum(current_num)
            for num in candidates:
                # print(current_num)
                if len(current_num)>0 and current_num[-1]>num:
                    continue
                
                total = s+num
                if total==target:
                    # l = sorted(current_num+[num])
                    l = current_num+[num]
                    if l not in res: 
                        res.append(l)
                elif total<target:
                    queue.append(current_num+[num])
        return res


            
        