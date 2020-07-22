from tkinter import *
from tkinter.colorchooser import askcolor

from prototype import GamePrototype


class Theme(Frame):
    def __init__(self, master=None, **configs):
        super().__init__(master, **configs)
        self.make_widgets()

    def make_widgets(self):
        self.lab3 = Label(self, text='Theme')
        self.lab3.grid(row=1, column=0, columnspan=3)
        self.ball_color = Button(self, text='Ball', height=3, width=7, bg='blue', command=self.ball_color_act)

        self.ball_color.grid(row=2, column=0, sticky=E)
        self.game_ball_color = 'blue'

        self.rackets_color = Button(self, text='Rackets', height=3, width=7, bg='red', command=self.rackets_color_act)
        self.rackets_color.grid(row=3, column=0, sticky=E)
        self.game_rackets_color = 'red'

        self.desk_prototipe = GamePrototype(self, width=200, height=110)
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

