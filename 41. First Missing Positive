class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        snums = set(nums)

        for i in range(1, 100002):
            if i not in snums:
                return i
        
        return 0
