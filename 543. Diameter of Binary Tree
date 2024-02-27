class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Variable to store the diameter
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0
            left_depth = depth(node.left)
            right_depth = depth(node.right)
            # Update diameter if necessary
            self.diameter = max(self.diameter, left_depth + right_depth)
            # Return the depth of the current node
            return 1 + max(left_depth, right_depth)
        
        depth(root)
        return self.diameter
