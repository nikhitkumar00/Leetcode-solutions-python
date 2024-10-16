class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            return True

        # Calculate the initial slope differences
        x_diff = coordinates[1][0] - coordinates[0][0]
        y_diff = coordinates[1][1] - coordinates[0][1]

        # Compare each consecutive slope using cross multiplication
        for i in range(2, len(coordinates)):
            x_diff_i = coordinates[i][0] - coordinates[i - 1][0]
            y_diff_i = coordinates[i][1] - coordinates[i - 1][1]

            if y_diff * x_diff_i != y_diff_i * x_diff:
                return False

        return True
