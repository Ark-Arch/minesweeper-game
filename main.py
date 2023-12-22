
from tkinter  import *
from settings import WIDTH         as window_width
from settings import HEIGHT        as window_height
from settings import GRID_SIZE     as grid_size
from utils    import width_prct    as width_resize
from utils    import height_prct   as height_resize
from cell     import Cell

root = Tk() # instantiating a window

# Override the settings of the window

root.title('MINESWEEPER') # providing a title for the game/window
root.geometry(f'{window_width}x{window_height}') # drawing up a size of the window
root.resizable(False, False) # to ensure that the size of the window cannot be resized
root.configure(bg='blue') # set a background color for the window


top_frame = Frame(
        root,
        bg='red', 
        width = width_resize(95),
        height = height_resize(8.333),
        )
top_frame.place(x=20, y=20)

left_frame = Frame(
        root,
        bg='green',
        width = width_resize(23.75),
        height = height_resize(85)
        )
left_frame.place(x = 20, y=70)

center_frame = Frame(
        root, 
        bg = 'yellow',
        width = width_resize(71.25),
        height = height_resize(85)
        )
center_frame.place(x = 210,y= 70)


for x in range(grid_size):
    for y in range(grid_size):
        unit_cell = Cell(x,y)
        unit_cell.create_btn_object(center_frame)
        unit_cell.cell_btn_object.grid(column=x, row=y)

print(Cell.get_cell_list_properties())

# Run the window
root.mainloop() # just to keep the window on until it is cancelled by the user
