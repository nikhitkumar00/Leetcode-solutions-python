class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        total_swaps = 0

        while q:
            level_size = len(q)
            level_values = []

            for i in range(level_size):
                node = q.popleft()
                level_values.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            swaps = 0
            target = sorted(level_values)

            pos = {val: i for i, val in enumerate(level_values)}

            for i in range(level_size):
                if level_values[i] != target[i]:
                    swaps += 1

                    cur = pos[target[i]]
                    pos[level_values[i]] = cur
                    level_values[cur] = level_values[i]

            total_swaps += swaps
        return total_swaps
