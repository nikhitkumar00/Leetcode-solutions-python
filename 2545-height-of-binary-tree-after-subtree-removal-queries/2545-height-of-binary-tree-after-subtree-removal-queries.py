# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        out = [0] * 100001
        self.cur_max = 0

        def left_to_right(node, cur):
            if not node:
                return

            out[node.val] = self.cur_max

            self.cur_max = max(self.cur_max, cur)

            left_to_right(node.left, cur + 1)
            left_to_right(node.right, cur + 1)

        def right_to_left(node, cur):
            if not node:
                return

            out[node.val] = max(out[node.val], self.cur_max)

            self.cur_max = max(cur, self.cur_max)

            right_to_left(node.right, cur + 1)
            right_to_left(node.left, cur + 1)

        left_to_right(root, 0)
        self.cur_max = 0
        right_to_left(root, 0)

        return [out[q] for q in queries]
