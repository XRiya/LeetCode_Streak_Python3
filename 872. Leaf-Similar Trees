class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Helper function to traverse the tree and collect leaf node values
        def checkLeaf(root, ans):
            # Base case: If the node is null, return
            if not root:
                return

            # Recursively check the left subtree
            checkLeaf(root.left, ans)

            # If the node is a leaf (both left and right children are null), add its value to the list
            if not root.left and not root.right:
                ans.append(root.val)

            # Recursively check the right subtree
            checkLeaf(root.right, ans)

        # Lists to store leaf values for each tree
        ans1, ans2 = [], []

        # Populate lists with leaf values using the helper function
        checkLeaf(root1, ans1)
        checkLeaf(root2, ans2)

        # Check if the leaf sequences for both trees are equal
        return ans1 == ans2
