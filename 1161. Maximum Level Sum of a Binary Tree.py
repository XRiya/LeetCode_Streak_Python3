class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> List[float]:
        level_sum = defaultdict(int)

        for lvl, val in self.inorder(root):
            level_sum[lvl + 1] += val

        return max(level_sum, key=lambda x: (level_sum[x], -x))

    @classmethod
    def inorder(cls, tree: TreeNode | None, level: int = 0):
        if tree is not None:
            yield from cls.inorder(tree.left, level + 1)
            yield level, tree.val
            yield from cls.inorder(tree.right, level + 1)
