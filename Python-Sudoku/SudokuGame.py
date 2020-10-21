from SudokuBoardGenerator import SudokuBoard
from SudokuExceptions import *
import random

class SudokuPuzzle (SudokuBoard):
    def __init__(self, difficulty = 0, max_num_solutions = 10):
        if  difficulty < 0 :
            raise Exception('Invalid Difficulty.  Min Difficulty == 1. Default Diffulty == 0')
        
        super().__init__()
        self.puzzle_board = super().getBoard().copy()
        self.original_board = super().getBoard().copy()
        self.difficulty = difficulty
        self.max_num_solutions = max_num_solutions
        self.solutions = []
        self.num_solutions = 0
        self.exponentCountSolutions = 10

    
    #difficulty is the defined by the number of times we go iterate through generatePuzzle
    def setDifficulty(self, difficulty:int):
        if difficulty == 0:
            #print('default difficulty error')
            raise DifficultyError (difficulty)
            #raise Exception('Cannot change difficulty to 0')
        if difficulty < 0:
            raise DifficultyError (difficulty)
            #raise Exception('Negative Difficulty Not Possible')
        
        
        self.difficulty = difficulty
        print('New difficulty\t',self.difficulty)

    #Use if you don't care how many solutions there would be to the puzzle
    def generateRandomPuzzle(self):
        print('Randomising')
        if self.difficulty == 0:
            raise Exception ('Puzzle Difficulty Not Set')
        else:
            for i in range (self.difficulty):
                #decides whether to add the 0s in the row, column or square
                #if 1 --> give every row a 0 at a random column index
                #if 2 --> give every column a 0 at a random row index
                #if 3 --> give every square a 0 at a random index
                #if 4 --> skip

                rand = random.randint(1,4) 
                
                if rand == 1: #gives every row a 0 at a random column index
                    for j in self.puzzle_board: 
                        randCol = random.randint(0,8)
                        j[randCol] = 0

                elif rand == 2: #gives every column a 0
                    for j in range(9):                    
                        randY = random.randint(0,8)
                        
                        count = 0
                        limit = 10
                        #makes sure a cell isn't already 0
                        #if we reach a limit of count, we give up
                        while self.puzzle_board[randY][j] == 0 and count < limit:
                            randY = random.randint(0,8)
                            count += 1
                        
                        self.puzzle_board[randY][j] = 0
                elif rand == 3: #gives every square a 0 
                    xMax = yMax = 2
                    xMin = yMin = 0

                    while xMax < 9:
                        while yMax < 9:
                            randX = random.randint(xMin,xMax)
                            randY = random.randint(yMin,yMax)

                            count = 0
                            limit = 10
                            #makes sure a cell isn't already 0
                            #if we reach a limit of count, we give up
                            while self.puzzle_board[randY][randX] == 0 and count < limit:
                                randX = random.randint(xMin,xMax)
                                randY = random.randint(yMin,yMax)
                                count += 1
                            
                            self.puzzle_board[randY][randX] = 0
                            
                            yMax += 3
                            yMin += 3
                        
                        xMax += 3
                        xMin += 3
                        yMin = 0
                        yMax = 2


    #Use if you want to limit the number of solutions to the puzzle
    def generateGoodPuzzle(self):
        
        print('Making Good Puzzle')

        self.generateRandomPuzzle()
        
        try:
            self.solve()
        except SolutionOverloadError:
            print('Too many Solutions')

            try:
                self.setDifficulty(self.difficulty - 1)
                self.__resetSolutions()
                self.generateGoodPuzzle()
            except DifficultyError:
                print('Difficulty error raised')
        
        
        # try:
            
        #     self.solve()
        #     print('Num solutions\t', self.num_solutions)
        # except SudokuExceptions.DifficultyError :
        #     pass:
        # except:
        #     print('Solve() found too many solutions')
        
        #     self.__resetSolutions()
        #     self.setDifficulty(self.difficulty - 1)
        #     self.generateGoodPuzzle()
            

        

    def possible(self, row:int, col:int, num:int):
        
        #if num is valid in the row
        if num in self.puzzle_board[row]:
            return False
        
        #if num is valid in the column
        for r in self.puzzle_board:
            if r[col] == num: 
                return False

        row0 = (row // 3) *3 #gets minimum square bound for row
        col0 = (col // 3) *3 #gets minimum square bound for col

        for i in range (0,3):
            for j in range(0,3):
                if self.puzzle_board[row0 + i][col0 + i] == num:
                    return False
        
        return True
        
        
    def solve(self):
        #print('Solving\t', self.num_solutions)
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
        self.solutions.append(self.__copyBoard(self.puzzle_board))
        
        if self.num_solutions == self.exponentCountSolutions:
            print('EEYYYY found a new table\t', self.num_solutions) 
            self.exponentCountSolutions *= 2
        
        if self.num_solutions == self.max_num_solutions:
            raise SolutionOverloadError()

    def __resetSolutions(self):
        print('resetting board')
        self.num_solutions = 0
        self.solutions.clear()
        self.puzzle_board = self.__copyBoard(self.original_board)
        self.exponentCountSolutions = 10

    #returns a deep copy of a board
    def __copyBoard(self, board):
        copy = []

        for row in self.board:
            copy_row = []
            for cell in row:
                copy_row.append(cell)
            copy.append(copy_row)

        return copy


            
