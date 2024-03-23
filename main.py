import tkinter as tk
from tkinter import *
from tkinter import messagebox

RES_X, RES_Y = 1920, 1008
CNTRL_X, CNTRL_Y = 1920, 206
MAP_X, MAP_Y = 1920, 800
TILE_SIZE = 16
TILE_NUM_X, TILE_NUM_Y = 120, 50
KM2_PER_TILE = 1

GRAY_WIN = '#323232'


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to exit?"):
        win.destroy()


win = Tk()
win.protocol("WM_DELETE_WINDOW", on_closing)
win.title("AoH")
win.config(bg=GRAY_WIN)
win.geometry(f"{RES_X}x{RES_Y}+0+0")
win.resizable(False, False)

photo = PhotoImage(file="res/AoH_2_icon.png")
win.iconphoto(False, photo)

cntrl_canvas = Canvas(win, width=CNTRL_X, height=CNTRL_Y, bg=GRAY_WIN, highlightthickness=0)
cntrl_canvas.pack()

map_canvas = Canvas(win, width=MAP_X, height=MAP_Y, bg=GRAY_WIN, highlightthickness=0)
map_canvas.pack()

img = PhotoImage(file="res/bg_game.png")
map_canvas.create_image(0, 0, anchor=NW, image=img)

tile_grid = [map_canvas.create_rectangle(x * TILE_SIZE, y * TILE_SIZE, x * TILE_SIZE + TILE_SIZE, y * TILE_SIZE + TILE_SIZE) for x in range (TILE_NUM_X) for y in range (TILE_NUM_Y)]

# fill=""

win.mainloop()
