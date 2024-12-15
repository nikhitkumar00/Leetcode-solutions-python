class Solution:
    def maxAverageRatio(self, classes, extraStudents):
        heap = []

        # Push negative improvement into the heap
        for p, t in classes:
            # Calculate improvement for one extra student
            improvement = -(((p + 1) / (t + 1)) - (p / t))
            heapq.heappush(heap, (improvement, p, t))

        # Distribute extra students
        for _ in range(extraStudents):
            # Pop the class with the highest potential improvement
            _, p, t = heapq.heappop(heap)

            # Add a student to the class
            p, t = p + 1, t + 1

            # Recalculate improvement and push back into the heap
            improvement = -(((p + 1) / (t + 1)) - (p / t))
            heapq.heappush(heap, (improvement, p, t))

        # Calculate the final average pass ratio
        total = 0
        for _, p, t in heap:
            total += p / t

        return total / len(classes)
