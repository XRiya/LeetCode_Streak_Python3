class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            return max(nums[i]+dp(i+2), dp(i+1))
        return dp(0)
