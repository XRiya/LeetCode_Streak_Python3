class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        curr = nums[0]
        count = 0

        for x in nums[1:]:
            if x == curr:
                count += 1

            else:
                count -= 1

            if count < 0:
                curr = x
                count = 0

        
        return curr
