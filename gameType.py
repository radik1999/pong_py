from tkinter import *

import game
from startscreen import *
from theme import Theme

class GameType(Frame):
    def __init__(self, parent=None, width=500, height=300, **configs):
        super().__init__(parent, width=width, height=height, **configs)
        self.width = width
        self.height = height
        self.make_widgets()

    def make_widgets(self):
        self.pack()

        self.theme = Theme(self)
        self.theme.pack(side=TOP)

        self.game_type = BooleanVar() # what type of game: solo - with computer or with someone
        self.rb_solo = Radiobutton(self, text='SOLO', variable=self.game_type, value=True)
        self.rb_solo.pack(side=LEFT)

        self.rb_with_some = Radiobutton(self, text='WITH SOMEONE', variable=self.game_type, value=False)
        self.rb_with_some.pack(side=LEFT)


        self.start = Button(self, text='Start', command=self.start_action)
        self.start.pack(side=TOP)


    def start_action(self):
        self.destroy()
        if self.game_type.get():
            StartScreen(self.master, self.width, self.height, self.theme.game_ball_color, self.theme.game_rackets_color)
        else:
            game.Game(self.master, self.width, self.height, None, 0, self.theme.game_ball_color, self.theme.game_rackets_color)

