from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_length = 0
        frequency = defaultdict(int)
        start = 0
        
        for end, num in enumerate(nums):
            frequency[num] += 1
            
            # If the frequency of any element exceeds k, adjust the window
            while frequency[num] > k:
                frequency[nums[start]] -= 1
                start += 1
            
            # Update the maximum length of the subarray
            max_length = max(max_length, end - start + 1)
        
        return max_length
