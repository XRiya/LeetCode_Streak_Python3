class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        arr=[root]
        ans=[[root.val]]
        while arr:
            a=[]
            b=[]
            for i in arr:
                if i.left:
                    a.append(i.left)
                    b.append(i.left.val)
                    
                if i.right:
                    a.append(i.right)
                    b.append(i.right.val)
            arr=a
            ans.append(b)
        # print(ans)
        return ans[-2][0]
