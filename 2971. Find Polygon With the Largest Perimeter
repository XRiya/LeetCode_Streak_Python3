class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
    
        arr=sorted(nums,reverse=True)
        perimiter=0
        n=len(arr)
        flag=0
        for i in range(n):
            for j in range(i+1,n):
                s=sum(arr[j:])
                if s>arr[i] and (n-j)+1>=3:
                    if s+arr[i]>perimiter:
                        perimiter=s+arr[i]
                    else:
                        flag=1
                        break
                else:
                    break
            if flag==1:
                break
        return perimiter if perimiter!=0 else -1
