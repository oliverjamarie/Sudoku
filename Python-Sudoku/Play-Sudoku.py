import tkinter as tk
from SudokuGame import SudokuPuzzle

class Test():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku")

        self.top_frame = tk.Frame(self.window)
        self.bot_frame = tk.Frame(self.window)


        self.label = tk.Label(master=self.top_frame, text="HOWDY BRUTHER What's your name?")
        self.label.pack()

        self.entry = tk.Entry(master=self.top_frame)
        self.entry.pack()

        self.btn = tk.Button(master=self.top_frame, text= "Submit", command= self.button_listener_name)
        self.btn.pack()

        self.name = tk.StringVar()
        self.disp_name = tk.Label(master=self.top_frame, text='Gimme a name')
        self.disp_name.pack()


        self.label2 = tk.Label(master=self.bot_frame, text="BOTTOM FRAME")
        self.label2.pack()

        self.top_frame.pack(side='right')
        self.bot_frame.pack(side='left')

        

        self.window.mainloop()

    def button_listener_name(self):
        self.disp_name['text'] = 'Well howdy ' + self.entry.get()

class Game():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title ('Sudoku')

        self.parent_frame= tk.Frame(self.window)

        self.frame_solution = tk.Frame(self.window)

        self.frame_board = tk.Frame(self.window)
        self.frame_board.grid(row=0,column=0)

        self.populate_board()
        
        
        self.frame_ui = tk.Frame(self.window)
        self.frame_ui.grid(row=0,column=1)

        self.btn_get_board= tk.Button(self.frame_ui, text='Generate New Board', command=self.gen_new_board)
        self.btn_get_board.pack()

        self.btn_get_solution= tk.Button(self.frame_ui, text="Get Solution", command= self.get_solution)
        self.btn_get_solution.pack()

        self.window.mainloop()

         

    def populate_board(self):
        self.sudoku = SudokuPuzzle (5)
        self.sudoku.generatePuzzle()
        
        for r in range(9):
            for c in range(9):
                if self.sudoku.board[r][c] != 0: 
                    cell = self.sudoku.board[r][c]
                    label = tk.Label(self.frame_board, text = cell, width=1, height =1)
                    label.grid(row=r, column= c)
                else:
                    entry = tk.Entry(self.frame_board)
                    entry.grid(row=r, column=c)

        for row in self.sudoku.board:
            print(row)

    def gen_new_board(self):

        self.frame_board.destroy()
        self.frame_board = tk.Frame(self.window)
        self.frame_board.grid(row=0,column=0)

        self.frame_solution.destroy()
        self.populate_board()
        
    def get_solution(self):
        self.frame_solution = tk.Frame(self.window)
        self.frame_solution.grid(row=1,column=0)

        for r in range(9):
            for c in range(9):
                cell = self.sudoku.original_board[r][c]
                label = tk.Label(self.frame_solution, text = cell)
                label.grid(row=r, column= c)


    def solve(self):
        self.frame_solution.destroy()
        self.frame_board.destroy()
        self.frame_board = tk.Frame(self.window)
        self.frame_board.grid(row=0,column=0)       

        for r in range(9):
            for c in range(9):
                cell = self.sudoku.original_board[r][c]
                label = tk.Label(self.frame_board, text = cell)
                label.grid(row=r, column= c)
    
    

game = Game()

