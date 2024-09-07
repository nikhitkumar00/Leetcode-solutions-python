class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        if self.compare(head, root):
            return True

        if not root:
            return False

        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    
    
    def compare(self, list_node, tree_node):
        
        if not list_node:
            return True

        if not tree_node or tree_node.val != list_node.val:
            return False

        return self.compare(list_node.next, tree_node.left) or self.compare(
            list_node.next, tree_node.right
        )
