class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        ROW, COL = len(box), len(box[0])

        rotated_box = [[0] * ROW for _ in range(COL)]
        for i in range(ROW):
            for j in range(COL):
                rotated_box[j][ROW - i - 1] = box[i][j]

        for j in range(ROW):  # COL of rotated box
            lowest_row = COL - 1
            for i in reversed(range(COL)):
                if rotated_box[i][j] == "#":
                    rotated_box[i][j] = "."
                    rotated_box[lowest_row][j] = "#"
                    lowest_row -= 1
                if rotated_box[i][j] == "*":
                    lowest_row = i - 1
        return rotated_box
