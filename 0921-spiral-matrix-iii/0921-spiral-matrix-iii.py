class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:

        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        row, col = rStart, cStart

        # Initialize the output list with the starting position
        out = [[rStart, cStart]]

        # Initialize the number of steps and the direction index
        steps = 1
        i = 0

        # Continue until all cells are visited
        while len(out) < rows * cols:
            
            # Get the current direction
            dr, dc = directions[i]

            # Move in the current direction for the specified number of steps
            for _ in range(steps):
                
                # Update the current position
                row, col = row + dr, col + dc

                # Check if the new position is within the grid boundaries
                if 0 <= row < rows and 0 <= col < cols:
                    # Add the new position to the output list
                    out.append([row, col])

            # Move to the next direction
            i = 0 if i == 3 else i + 1

            # Increment the number of steps after every two directions
            steps += 1 if i % 2 == 0 else 0

        return out
