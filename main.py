
from tkinter import *


root = Tk() # instantiating a window
root.title('MINESWEEPER') # providing a title for the game/window
root.geometry('800x400') # drawing up a size of the window
root.resizable(False, False) # to ensure that the size of the window cannot be resized
root.configure(bg='blue') # set a background color for the window
root.mainloop() # just to keep the window on until it is cancelled by the user
