class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        lvl = []
        q = deque([root])

        while q:
            summ = 0
            for _ in range(len(q)):
                node = q.popleft()
                summ += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            lvl.append(summ)

        q.append(root)
        root.val = 0
        i = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                sib_sum = (node.left.val if node.left else 0) + (
                    node.right.val if node.right else 0
                )

                if node.left:
                    node.left.val = lvl[i] - sib_sum
                    q.append(node.left)
                if node.right:
                    node.right.val = lvl[i] - sib_sum
                    q.append(node.right)
            i += 1

        return root
