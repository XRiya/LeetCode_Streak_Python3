from typing import *

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        result = [0]*len(nums)

        current_positive_index = 0
        current_negative_index = 1

        for num in nums:
            if num > 0:
                result[ current_positive_index ] = num
                current_positive_index += 2
            if num < 0:
                result[ current_negative_index ] = num
                current_negative_index += 2

        return( result )
