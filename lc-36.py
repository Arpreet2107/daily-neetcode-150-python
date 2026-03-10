class Solution:
    def isValidSudoku(self, board):

        # Create sets to track numbers in rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Loop through each cell of the board
        for r in range(9):
            for c in range(9):

                # Get the value at the current cell
                val = board[r][c]

                # Skip empty cells represented by "."
                if val == ".":
                    continue

                # Determine which 3x3 box the cell belongs to
                box_index = (r // 3) * 3 + (c // 3)

                # Check if number already exists in row, column, or box
                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False

                # Add the value to corresponding row, column, and box sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        # If no rule is violated, the Sudoku board is valid
        return True