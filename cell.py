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
        self.cell_btn_object = btn
