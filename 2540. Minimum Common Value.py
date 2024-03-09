class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        candidate = set(nums1) & set(nums2)
        if not candidate:
            return -1
        
        return min(candidate)
