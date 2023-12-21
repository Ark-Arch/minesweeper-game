from tkinter import Button


class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_btn_object(self, container):
        btn = Button(
                container,
                text = 'Text',
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
