class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums1.extend(nums2)
        nums1.sort()
        m  = len(nums1)
        if m %2 == 0 :
            return (nums1[int(m/2)] + nums1[int((m - 1)/2)])/ 2
        
        return nums1[int(m/2)]