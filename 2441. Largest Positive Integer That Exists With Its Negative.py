class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        sm = [0] * 1001
        maxi = -1
        for n in nums:
            idx = n if n > 0 else -n
            if sm[idx] != n:
                sm[idx] += n
            if sm[idx] == 0:
                maxi = maxi if maxi > idx else idx
        return maxi
