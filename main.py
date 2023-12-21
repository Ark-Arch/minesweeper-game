
from tkinter import *


root = Tk() # instantiating a window

# Override the settings of the window

root.title('MINESWEEPER') # providing a title for the game/window
root.geometry('800x600') # drawing up a size of the window
root.resizable(False, False) # to ensure that the size of the window cannot be resized
root.configure(bg='blue') # set a background color for the window


top_frame = Frame(
        root,
        bg='red', 
        width = 760,
        height = 50,
        )
top_frame.place(x=20, y=20)

left_frame = Frame(
        root,
        bg='green',
        width = 190,
        height = 510
        )
left_frame.place(x = 20, y=70)


# Run the window
root.mainloop() # just to keep the window on until it is cancelled by the user
