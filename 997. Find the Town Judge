class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        c = [Counter(a) for a in zip(*trust)] if trust else [Counter()] * 2

        return next((i for i in range(1,n+1) if c[0][i]==0 and c[1][i]==n-1), -1)
