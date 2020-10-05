import tkinter
from tkinter import *
from GameDesk import Desk
from game import Game
from startscreen import StartScreen
from prototype import GamePrototype
from gameType import *

root = Tk()
root.geometry('500x300+350+150')

GameType(root)
# StartScreen(root, width=700, height=400)

root.mainloop()
