from  tkinter   import Button
import random
from  settings  import MINES_COUNT   as  no_of_mines

class Cell:
    all = [] #this is a class attribute a collection of all instances created
    def __init__(self, x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append every cell object to the cell.all class attribute list
        Cell.append_cell(self)
        # i could have easily written the below => Cell.all.append(self)


    # INSTANE METHODS
    def __str__(self):
        return f"{self.x},{self.y}"

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"

    def create_btn_object(self, container):
        btn = Button(
                container,
                width = 8,
                height = 4,
                text = self.__str__(),
                bg = 'pink'
                )

        btn.bind('<Button-1>', self.left_click_response)
        btn.bind('<Button-3>', self.right_click_response)
        self.cell_btn_object = btn

    def left_click_response(self, event):
        print(event)
        print("I am left clicked!")

    def right_click_response(self, event):
        print(event)
        print("I am right clicked")


    # CLASS METHODS
    @classmethod
    def append_cell(cls, cell):
        cls.all.append(cell)

    @classmethod
    def get_cell_list(cls):
        return cls.all


    # STATIC METHOD
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(  # this then becomes a list of Cell objects
                Cell.get_cell_list(),
                no_of_mines,
                )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

