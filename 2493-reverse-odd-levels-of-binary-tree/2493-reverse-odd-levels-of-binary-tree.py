class Solution:
    def reverseOddLevels(self, root):
        def traverse(left, right, even):
            if left is None or right is None:
                return

            if even:
                temp = left.val
                left.val = right.val
                right.val = temp

            traverse(left.left, right.right, not even)
            traverse(left.right, right.left, not even)

        traverse(root.left, root.right, True)
        return root
