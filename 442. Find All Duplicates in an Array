class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        nums.sort()
        i=0
        j=1
        if len(nums)==1:
            return []
        while i<len(nums) and j<len(nums):
            if nums[i]==nums[j]:
                ans.append(nums[i])
                i+=2
                j+=2
                
            else:
                i+=1
                j+=1
        return ans
