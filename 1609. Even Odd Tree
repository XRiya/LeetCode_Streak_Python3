class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        q = deque([root])
        curr_level = 0
        while q:
            last_node = None
            for _ in range(len(q)):
                node = q.popleft()
                if (curr_level % 2 and (node.val % 2 or (last_node and node.val >= last_node))) or \
                    (not curr_level % 2 and (not node.val % 2 or (last_node and node.val <= last_node))):
                    return False
                last_node = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            curr_level += 1
        return True
