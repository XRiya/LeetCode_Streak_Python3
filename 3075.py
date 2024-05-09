class Solution(object):
    def maximumHappinessSum(self, h, k):
        h.sort(reverse=True)
        res = 0
        for i in range(min(len(h), k)):
            if h[i] <= i:
                break
            res += h[i] - i
        return res
        
