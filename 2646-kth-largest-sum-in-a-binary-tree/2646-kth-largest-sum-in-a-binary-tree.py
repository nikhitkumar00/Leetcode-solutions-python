class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        heap = []

        while q:
            summ = 0
            for i in range(len(q)):
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
