class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        i = 0
        j = 0
        
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        
        while i<len(nums1):
            res.append(nums1[i])
            i+=1
        
        while j<len(nums2):
            res.append(nums2[j])
            j+=1
        
        t = 0
        l = len(res)//2
        
        if len(res)%2==0:
            t = (res[l]+res[l-1])/2
        else:
            t = res[l]
        
        return t