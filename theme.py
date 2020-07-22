from tkinter import *
from tkinter.colorchooser import askcolor

from prototype import GamePrototype


class Theme(Frame):
    def __init__(self, master=None, bcolor='blue', rcolor='red', **configs):
        super().__init__(master, **configs)
        self.game_ball_color = bcolor
        self.game_rackets_color = rcolor
        self.make_widgets()


    def make_widgets(self):
        self.lab3 = Label(self, text='Theme')
        self.lab3.grid(row=1, column=0, columnspan=3)

        self.ball_color = Button(self, text='Ball', height=3, width=7, bg=self.game_ball_color, command=self.ball_color_act)
        self.ball_color.grid(row=2, column=0, sticky=E)

        self.rackets_color = Button(self, text='Rackets', height=3, width=7, bg=self.game_rackets_color, command=self.rackets_color_act)
        self.rackets_color.grid(row=3, column=0, sticky=E)

        self.desk_prototipe = GamePrototype(self, width=200, height=110, ball_color=self.game_ball_color, rackets_color=self.game_rackets_color)
        self.desk_prototipe.desk.grid(row=2, column=1, columnspan=2, rowspan=2, sticky=W)


    def ball_color_act(self):
        color = askcolor()[1]
        self.game_ball_color = color
        self.ball_color.config(bg=color)
        self.desk_prototipe.desk.itemconfigure(self.desk_prototipe.ball.id, fill=color)

    def rackets_color_act(self):
        color = askcolor()[1]
        self.game_rackets_color = color
        self.rackets_color.config(bg=color)
        self.desk_prototipe.desk.itemconfigure(self.desk_prototipe.player1.id, fill=color)
        self.desk_prototipe.desk.itemconfigure(self.desk_prototipe.player2.id, fill=color)

