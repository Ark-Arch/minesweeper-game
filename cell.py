from tkinter import Button


class Cell:
    def __init__(self, x,y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y


    def __str__(self):
        return f"{self.x},{self.y}"

    # INSTANE METHODS
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
