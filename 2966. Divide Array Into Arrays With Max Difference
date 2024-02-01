class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0,len(nums),3):
            if nums[i+1]-nums[i]<=k and nums[i+2]-nums[i+1]<=k and nums[i+2]-nums[i]<=k:
                ans.append(nums[i:i+3])
            else:
                return []
        return ans
