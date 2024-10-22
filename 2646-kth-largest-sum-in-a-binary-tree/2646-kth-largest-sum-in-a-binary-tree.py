# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        q.append(root)
        heap = []

        while q:
            summ = 0
            size = len(q)
            for i in range(size):
                node = q.popleft()
                summ += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            heapq.heappush(heap, summ)
            if len(heap) > k:
                heapq.heappop(heap)

        return -1 if len(heap) < k else heap[0]
