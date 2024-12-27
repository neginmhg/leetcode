"""
Hard

Topics

Companies
Design the basic function of Excel and implement the function of the sum formula.

Implement the Excel class:

Excel(int height, char width) Initializes the object with the height and the width of the sheet. The sheet is an integer matrix mat of size height x width with the row index in the range [1, height] and the column index in the range ['A', width]. All the values should be zero initially.
void set(int row, char column, int val) Changes the value at mat[row][column] to be val.
int get(int row, char column) Returns the value at mat[row][column].
int sum(int row, char column, List<String> numbers) Sets the value at mat[row][column] to be the sum of cells represented by numbers and returns the value at mat[row][column]. This sum formula should exist until this cell is overlapped by another value or another sum formula. numbers[i] could be on the format:
"ColRow" that represents a single cell.
For example, "F7" represents the cell mat[7]['F'].
"ColRow1:ColRow2" that represents a range of cells. The range will always be a rectangle where "ColRow1" represent the position of the top-left cell, and "ColRow2" represents the position of the bottom-right cell.
For example, "B3:F7" represents the cells mat[i][j] for 3 <= i <= 7 and 'B' <= j <= 'F'.
Note: You could assume that there will not be any circular sum reference.

For example, mat[1]['A'] == sum(1, "B") and mat[1]['B'] == sum(1, "A").
 

Example 1:

Input
["Excel", "set", "sum", "set", "get"]
[[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]
Output
[null, null, 4, null, 6]

Explanation
Excel excel = new Excel(3, "C");
 // construct a 3*3 2D array with all zero.
 //   A B C
 // 1 0 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.set(1, "A", 2);
 // set mat[1]["A"] to be 2.
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 0
excel.sum(3, "C", ["A1", "A1:B2"]); // return 4
 // set mat[3]["C"] to be the sum of value at mat[1]["A"] and the values sum of the rectangle range whose top-left cell is mat[1]["A"] and bottom-right cell is mat[2]["B"].
 //   A B C
 // 1 2 0 0
 // 2 0 0 0
 // 3 0 0 4
excel.set(2, "B", 2);
 // set mat[2]["B"] to be 2. Note mat[3]["C"] should also be changed.
 //   A B C
 // 1 2 0 0
 // 2 0 2 0
 // 3 0 0 6
excel.get(3, "C"); // return 6
 
"""
"""
Example
    grid = {
        "A1": 2,  # Direct Value
        "B2": 5,  # Direct Value
        "C3": 7   # Computed Value (Sum of A1 + B2 + B3)
    }
    dependencies = {
        "C3": {"A1", "B2", "B3"}  # Tracks dependency for updates
    }
"""
class Excel:

    def __init__(self, height: int, width: str):
        #Store cell values
        self.grid ={}           #colRow : int value
        #Store dependencies for sum formula
        self.dependencies = {}      #colRow: list of colRows
        # Calculate the max column as an integer (A = 1, B = 2, ...)
        self.maxCol = ord(width)-ord('A')+1
    def set(self, row: int, column: str, val: int) -> None:
        if (row, column) in self.dependencies:
            del self.dependencies[(row,column)]
        self.grid[(row, column)]=val

    def get(self, row: int, column: str) -> int:
        if (row, column) in self.dependencies:
            return self.calculateSum(self.dependencies[(row,column)])
        return self.grid.get([(row,column)],0)
    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        self.dependencies[(row,column)] = numbers
        total = self.calculateSum(numbers)
        self.grid[(row,column)] =total
        return total
    
    def calculateSum(self,numbers):
        total = 0
        for item in numbers:
            if ':' in item:  # Range specified
                start, end = item.split(':')
                start_row, start_col = int(start[1:]), start[0]
                end_row, end_col = int(end[1:]), end[0]
                for r in range(start_row, end_row + 1):
                    for c in range(ord(start_col), ord(end_col) + 1):
                        total += self.get(r, chr(c))
            else:  # Single cell specified
                r, c = int(item[1:]), item[0]
                total += self.get(r, c)
        return total


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)