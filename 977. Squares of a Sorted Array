class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        stack = []
        ans = []
    
        for num in nums:
            if num < 0:
                stack.append(-num)
            else:
                while stack and num > stack[-1]:
                    ans.append(stack.pop()**2)
                
                ans.append(num**2)
        
        while stack:
            ans.append(stack.pop()**2)

        return ans
