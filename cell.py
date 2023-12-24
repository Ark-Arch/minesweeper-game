from  tkinter   import Button
from  tkinter   import messagebox as mb
from  tkinter   import Label
import random
from  settings  import MINES_COUNT   as  no_of_mines
from  settings  import CELL_COUNT    as  no_of_cells

import os 
import sys
import ctypes

class Cell:
    all = [] #this is a class attribute a collection of all instances created
    cell_count_label_object = None
    cell_count = no_of_cells
    def __init__(self, x,y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.original_button_color = None
        self.x = x
        self.y = y

        # Append every cell object to the cell.all class attribute list
        Cell.append_cell(self)
        # i could have easily written the below => Cell.all.append(self)
    
    #Getter
    @property
    def surrounding_cells(self):
        _surrounding_cells = []

        x = [self.x-1, self.x, self.x+1]
        y = [self.y-1, self.y, self.y+1]

        for i in x:
            for j in y:
                _surrounding_cells.append(Cell.get_cell_by_coordinates(i,j))

        _surrounding_cells.remove(self)

        _surrounding_cells = [cell for cell in _surrounding_cells if cell is not None]
        return _surrounding_cells

    @property
    def get_length_of_surrounding_mine_cells(self):
        return len( [cell for cell in self.surrounding_cells if cell.is_mine is True] )

    # INSTANCE METHODS
    def __str__(self):
        return f"{self.x},{self.y}"

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"

    def create_btn_object(self, container):
        btn = Button(
                container,
                width = 8,
                height = 4,
                #text = self.__str__(),
                bg = 'pink'
                )
        self.original_button_color = btn.cget("background")

        # the buttons are bound to the functions
        btn.bind('<Button-1>', self.left_click_response)
        btn.bind('<Button-3>', self.right_click_response)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(container):
        lbl = Label(
        	container,
            text = f"Safe Cells Left: {Cell.cell_count}",
            bg = 'black',
            fg = 'white',
            font=("", 14)
        )
        Cell.cell_count_label_object = lbl


    def show_mine(self):
        # write a logic that interruppts the game
        # and that displays a message that the play has lost!

        # during development, it suffices to change the bg color
        self.cell_btn_object.configure(bg = 'red')
        #ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        self.cell_btn_object.configure(command = Cell.game_over)

    

    def show_no_of_surrounding_mine_cells(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            print(self.get_length_of_surrounding_mine_cells)
            self.cell_btn_object.configure(text = self.get_length_of_surrounding_mine_cells)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                        text = f"Cells Left: {Cell.cell_count}"
                        )
            # if it was considered a possible mine, then it makes sense to reconfigure the background color
            self.cell_btn_object.configure(
                    bg = self.original_button_color
                    )
        self.is_opened = True



    def left_click_response(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.get_length_of_surrounding_mine_cells == 0:
                for cell in self.surrounding_cells:
                    cell.show_no_of_surrounding_mine_cells()
            self.show_no_of_surrounding_mine_cells()


    def right_click_response(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                    bg = "orange"
                    )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                    bg = self.original_button_color
                    )
            self.is_mine_candidate = False



    # CLASS METHODS
    @classmethod
    def append_cell(cls, cell):
        cls.all.append(cell)

    @classmethod
    def get_cell_list(cls):
        return cls.all

    @classmethod
    def get_cell_by_coordinates(cls, x, y):
        # return a cell object based on the values of x and y
        for cell in cls.all:
            if cell.x == x and cell.y == y:
                return cell


    # STATIC METHOD
    @staticmethod
    def game_over():
        note = "Sorry, you've clicked on a mine.\nWould you like to retry the game?"
        if mb.askyesno("GAME OVER", note):
            #wrote a script to restart the game
            os.execl(sys.executable,'python3', 'main.py', *sys.argv[1:])
        else:
            mb.showinfo("YOU GAVE UP!", "You have quit the game")
            sys.exit()

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(  # this then becomes a list of Cell objects
                Cell.get_cell_list(),
                no_of_mines,
                )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

