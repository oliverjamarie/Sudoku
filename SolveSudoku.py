from SudokuGame import SudokuPuzzle

class Solver:
    def __init__(self, puzzle: SudokuPuzzle, max_num_solutions = 1000):
        self.game = puzzle
        self.board = puzzle.board.copy()
        self.num_solutions = 0
        self.exponentCountSolutions = 10
        self.max_num_solutions = max_num_solutions
        self.solutions = []

    def possible(self, row:int, col:int, num:int):
        
        #if num is valid in the row
        if num in self.board[row]:
            return False
        
        #if num is valid in the column
        for r in self.board:
            if r[col] == num: 
                return False

        row0 = (row // 3) *3 #gets minimum square bound for row
        col0 = (col // 3) *3 #gets minimum square bound for col

        for i in range (0,3):
            for j in range(0,3):
                if self.board[row0 + i][col0 + i] == num:
                    return False
        
        return True

    def solve(self):
        for row in range (9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range (1,10): #numbers between 1 and 10
                        if self.possible(row,col,num) == True:
                            self.board[row][col] = num #tries to solve the board with num
                            self.solve()

                            self.board[row][col] = 0 #if num is not the correct answer, reset the cell to 0
                    return

        self.num_solutions += 1
        self.solutions.append(self.__copyBoard())

        if self.num_solutions == self.exponentCountSolutions:
            print('EEYYYY found a new table\t', self.num_solutions) 
            self.exponentCountSolutions *= 2
        
        if self.num_solutions == self.max_num_solutions:
            raise Exception ('Board has too many solutions. Not a good board')
        
        
    #returns a deep copy of a board
    def __copyBoard(self):
        copy = []

        for row in self.board:
            copy_row = []
            for cell in row:
                copy_row.append(cell)
            copy.append(copy_row)

        return copy
        