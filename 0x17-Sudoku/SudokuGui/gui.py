'''
GUI which allows you to solve any Sudoku puzzle.

The GUI has been created using Tkinter and a backtracking algorithm has been used.
'''

from tkinter import *

root = Tk()
root.geometry('330x370')
  
# Sudoku solver class
class SudokuSolver():

    def __init__(self):
        self.setZero()
        self.solve()
        
    # Set the empty cells to 0 (i.e. the cells you have not filled in)
    def setZero(self):
        for i in range(9):
            for j in range(9):
                if filledBoard[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    filledBoard[i][j].set(0)

    # Solve using backtracking    
    def solve(self):
        # Find next empty cell
        findEmpty = self.emptyCell()
        
        if not findEmpty:
            return True   
        else:
            row, column = findEmpty
        
        for i in range(1,10):
            if self.isValid(i, (row, column)):
                filledBoard[row][column].set(i)

                if self.solve():
                    return True

                filledBoard[row][column].set(0)
        
        return False

    # Check row, column and subgrid(3x3 square) to see if number can be placed in cell          
    def isValid (self, num, pos):
        # Check Row
        for i in range(9):
            if filledBoard[pos[0]][i].get() == str(num):
                return False
        # Check Column 
        for i in range(9):
            if filledBoard[i][pos[1]].get() == str(num):
                return False

        # Check Sub Grid
        row = pos[0] // 3 
        column = pos[1] // 3 

        for i in range(row * 3, (row * 3) + 3):
            for j in range(column * 3, (column * 3) + 3):
                if filledBoard[i][j].get() == str(num):
                    return False 
        return True

    # Find empty cells, defined as cells filled with a zero
    def emptyCell(self):
        for row in range(9):
            for column in range(9):
                if filledBoard[row][column].get() == '0':
                    return (row,column)
        return None

# GUI class
class Interface():
    def __init__(self, window):
        self.window = window
        window.title("Sudoku Solver")

        font = ('Arial', 20)
        color = 'white'

        # Create solve and clear button and link them to Solve and Clear methods
        solve = Button(window, text = 'Solve', command = self.Solve)
        solve.grid(column=3,row=20)
        clear = Button(window, text = 'Clear', command = self.Clear)
        clear.grid(column = 5,row=20)

        # Initialise empty 2D list
        self.board  = []
        for row in range(9):
            self.board += [["","","","","","","","",""]]

        for row in range(9):
            for col in range(9):
                # Change color of cells depending on position in grid
                if (row < 3 or row > 5) and (col < 3 or col > 5):
                    color = 'white' 
                elif (row >= 3 and row < 6) and (col >=3 and col < 6):
                    color = 'white'
                else:
                    color = 'grey'
                
                # Make each cell of grid a entry box and store each user entry into the filledBoard 2D list
                self.board[row][col] = Entry(window, width = 2, font = font, bg = color, cursor = 'arrow', borderwidth = 2,
                                          highlightcolor = 'yellow', highlightthickness = 0, highlightbackground = 'black', 
                                          textvariable = filledBoard[row][col]) 
                self.board[row][col].bind('<FocusIn>', self.gridChecker) # Link to better understand binding statements: https://www.python-course.eu/tkinter_events_binds.php#:~:text=Tkinter%20provides%20a%20mechanism%20to,and%20methods%20to%20an%20event.&text=If%20the%20defined%20event%20occurs,describing%20the%20event.
                self.board[row][col].bind('<Motion>', self.gridChecker)                        
                self.board[row][col].grid(row = row, column = col)

    # Function to check if user enters a value which is not an int between 1 and 9 (valid numbers in Sudoku game).
    # If entry is not valid, clear value
    def gridChecker(self, event):
        for row in range(9):
            for col in range(9):
                if filledBoard[row][col].get() not in ['1','2','3','4','5','6','7','8','9']:
                    filledBoard[row][col].set('')

    # Call Sudoku solver class (called by solve button)
    def Solve(self):
        SudokuSolver()

    # Function to clear board (called by clear button) 
    def Clear(self):
        for row in range(9):
            for col in range(9):
                filledBoard[row][col].set('')

# Global 2D list which saved in the values the user enters on the GUI
# Each value in the 2D list is set as a StringVar(), a class in Tkinter
# which allows you to save values users enter into the Entry widget
filledBoard = []
for row in range(9): 
    filledBoard += [["","","","","","","","",""]]
for row in range(9):
    for col in range(9):
        filledBoard[row][col] = StringVar(root)    

# Main Loop
Interface(root)
root.mainloop()



