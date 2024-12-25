class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        out = []
        q = deque([root])

        while q:
            size = len(q)
            level_max = float("-inf")
            for _ in range(size):
                node = q.popleft()
                level_max = max(level_max, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            out.append(level_max)
        return out
