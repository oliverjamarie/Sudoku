import random

class SudokuBoard:
    def __init__(self):
        self.board = []
        self.invalid_cells = []
        self.__generateBoard()
        self.__solveBoard()

    def __generateBoard(self):
        for i in range (0,9):
            row = []
            for j in range (0,9):
                rand = random.randint(1,9)
                row.append(rand)
            self.board.append(row)
        
    def __solveBoard(self):
        count_swaps = -1
        count_attempts = 0
        is_solved = False
        exponent = 10

        while is_solved == False:
            count_swaps = 0
            for x in range (0,9):
                for y in range (0,9):
                    num = self.board[x][y]
                    if self.__validCell(num,x,y) == False:
                        self.invalid_cells.append({'x':x, 'y':y})
                        count_swaps += 1
            
            count_attempts +=1
            if len(self.invalid_cells) == 0:
                print('SUCCESS\t Made table in\t%d\tattempts'%count_attempts)
                is_solved = True
            else:
                #print ('Solving attempt\t#',count_attempts)
                self.__attemptSolve()

    def __getPossibleValuesFromRow(self, row:int):
        possible_values = [1,2,3,4,5,6,7,8,9]

        for num in self.board[row]:
            if num != 0 and num in possible_values:
                possible_values.remove(num)
        
        return possible_values

    def __getPossibleValuesFromCol (self, col:int):
        possible_values = [1,2,3,4,5,6,7,8,9]

        for row in self.board:
            if row[col] != 0 and row[col] in possible_values:
                possible_values.remove(row[col])
        
        return possible_values

    def __getPossibleValuesFromSquare(self, row:int, col:int):
        numbers_in_square = self.__getNumbersInSquare(row,col)
        possible_values = [1,2,3,4,5,6,7,8,9]

        for num in numbers_in_square:
            if num != 0 and num in possible_values:
                possible_values.remove(num)

        return possible_values
        
    def getBoard(self):
        return self.board.copy()

    def __str__(self):
        string = ''

        for row in self.board:
            string += str(row)
            string += '\n'
        
        return string

    def __attemptSolve(self):

        for cell in self.invalid_cells:
            x = cell['x']
            y = cell['y']

            possible_values = self.__getPossibleValues(x,y)
            try:
                rand = random.choice(possible_values)
            except:
                #print('Empty list of possible values')
                rand  = random.randint(1,9)
            self.board[x][y] = rand

        self.invalid_cells.clear()

    def __getPossibleValues(self, row:int, col:int):
        possible_values = []
        all_possible_values = []

        poss_row = self.__getPossibleValuesFromRow(row) #Possible values in row
        poss_col = self.__getPossibleValuesFromCol(col) #Possible values in column
        poss_square = self.__getPossibleValuesFromSquare(row,col) #Possible values in the square

        all_possible_values = poss_row + poss_col + poss_square

        #A number is only considered possible if it can be found in 
        # poss_row AND poss_col AND poss_square
        for num in all_possible_values:
            if num in poss_row and num in poss_col and num in poss_square:
                possible_values.append(num)

        return possible_values

    def __validCell(self, num: int, x:int, y:int):
        
        if self.__isRowValid(x) == False:
            self.board[x][y] = 0
            return False
        elif self.__isColValid(y) == False:
            self.board[x][y] = 0
            return False
        elif self.__isSquareValid(x,y) == False:
            self.board[x][y] = 0
            return False

        return True
    
    def __isRowValid(self, row:int):
        numbers_encountered = []

        for num in self.board[row]:
            if num in numbers_encountered:
                return False
            else :
                numbers_encountered.append(num)
        
        return True
 
    def __isColValid(self, col:int):
        numbers_encountered = []

        for row in self.board:
            if row[col] in numbers_encountered:
                return False
            else:
                numbers_encountered.append(row[col])

        return True

    def __isSquareValid(self, row:int, col:int):
        numbers_in_square = self.__getNumbersInSquare(row,col)
        numbers_encountered = []

        for num in numbers_in_square:
            if num in numbers_encountered:
                return False
            else:
                numbers_encountered.append(num)

        return True


    def __getNumbersInSquare(self, row:int, col:int):
        numbers = []
        bounds = self.__getSquareBounds(row,col)

        for x in range(bounds.X_min, bounds.X_max):
            for y in range(bounds.Y_min, bounds.Y_max):
                numbers.append(self.board[x][y])

        return numbers

    def __getSquareBounds(self, row:int, col:int):
        if row < 3:
            if col < 3:
                bounds = Bound(0,3,0,3)
                return bounds
            elif col < 6:
                bounds = Bound(0,3,3,6)
                return bounds
            elif col < 6:
                bounds = Bound(0,3,6,9)
                return bounds
        elif row < 6:
            if col < 3:
                bounds = Bound(3,6,0,3)
                return bounds
            elif col < 6:
                bounds = Bound(3,6,3,6)
                return bounds
            elif col < 6:
                bounds = Bound(3,6,6,9)
                return bounds
        elif row < 9:
            if col < 3:
                bounds = Bound(6,9,0,3)
                return bounds
            elif col < 6:
                bounds = Bound(6,9,3,6)
                return bounds
            elif col < 6:
                bounds = Bound(6,9,6,9)
                return bounds

        return Bound(0,0,0,0)



class Bound:
    def __init__(self, x_min:int, x_max:int, y_min:int, y_max:int):
        self.X_min = x_min
        self.X_max = x_max
        self.Y_min = y_min
        self.Y_max = y_max
