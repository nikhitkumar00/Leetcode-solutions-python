class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        adj = {
            0: (1, 3),
            1: (0, 4, 2),
            2: (1, 5),
            3: (0, 4),
            4: (3, 1, 5),
            5: (2, 4),
        }

        board = [v for r in board for v in r]
        q = deque([(board.index(0), board, 0)])  # index, board, moves
        visited = set()

        while q:
            index, board, moves = q.popleft()

            if board == [1, 2, 3, 4, 5, 0]:
                return moves

            for neighbour in adj[index]:
                new = board[:]
                new[index], new[neighbour] = board[neighbour], board[index]

                if tuple(new) not in visited:
                    q.append((neighbour, new, moves + 1))
                    visited.add(tuple(new))

        return -1
