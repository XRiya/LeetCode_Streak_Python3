class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        m,n= 0,0
        d = {}
        for i in range(len(nums)):
            if(nums[i]==0):
                n-=1
            else:
                n+=1
            if(n not in d):
                d[n] = i
            else:
                a = i-d[n]
                if(a>m):
                    m=a
            if(n==0):
                if(i+1>m):
                    m=i+1

        return m
