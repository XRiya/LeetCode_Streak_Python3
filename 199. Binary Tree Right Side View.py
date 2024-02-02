class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        depth = 0
        

        def rightSide(root , result , depth):
            if root == None:
                return

            if len(result) == depth :
                result.append(root.val)

            depth += 1        

            rightSide(root.right , result , depth)
            rightSide(root.left , result , depth)

        rightSide(root , result , depth)
        return result   
