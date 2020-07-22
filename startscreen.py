from tkinter import *
import game
from prototype import GamePrototype
from tkinter.colorchooser import askcolor


class StartScreen(Frame):
	def __init__(self, parent=None, width=500, height=300, bcolor='blue', rcolor='red', **configs):
		super().__init__(parent, width=width, height=height, **configs)
		self.width = width
		self.height = height
		self.bcolor = bcolor
		self.rcolor = rcolor
		self.pack()
		self.make_widgets()
		self.focus_set()
		self.bind('<Return>', self.start_new_game)

	def make_widgets(self):
		self.rowconfigure(0, weight=1)
		self.rowconfigure(1, weight=1)
		self.rowconfigure(2, weight=1)
		self.rowconfigure(3, weight=1)
		self.rowconfigure(4, weight=1)
		self.rowconfigure(5, weight=1)
		self.rowconfigure(6, weight=1)
		self.rowconfigure(7, weight=1)
		self.columnconfigure(0, weight=1, pad=40)
		self.columnconfigure(1, weight=1, pad=100)
		self.columnconfigure(2, weight=1, pad=50)
		# self.columnconfigure(3, weight=1)
		# self.columnconfigure(4, weight=1)

		self.lab1 = LLabel(self, text='Side')
		self.lab1.grid(row=0, column=0, columnspan=2, sticky=NSEW)

		self.side = BooleanVar()
		self.rb_left = RRadiobutton(self, text='left', variable=self.side, value=False)
		self.rb_left.grid(row=1, column=0)

		self.rb_right = RRadiobutton(self, text='right', variable=self.side, value=True)
		self.rb_right.grid(row=1, column=1)


		self.difficult = IntVar()
		self.lab2 = LLabel(self, text='Difficult')
		self.lab2.grid(row=0, column=2)

		self.rb_easy = RRadiobutton(self, text='easy    ', variable=self.difficult, value=1)
		self.rb_easy.grid(row=1, column=2)

		self.rb_middle = RRadiobutton(self, text='middle', variable=self.difficult, value=2)
		self.rb_middle.grid(row=2, column=2)
		self.rb_middle.select()

		self.rb_hard = RRadiobutton(self, text='hard    ', variable=self.difficult, value=3)
		self.rb_hard.grid(row=3, column=2)


		self.start_game = Button(self, text='Start', font=('Times', 14, 'bold'), command=self.start_new_game)
		self.start_game.grid(row=7, column=0, sticky=NSEW)
		self.quit_but = Button(self, text='Exit', font=('Times', 14, 'bold'),command=lambda: self.master.destroy())
		self.quit_but.grid(row=7, column=2, sticky=NSEW)

	def start_new_game(self, event=None):
		# print(self.side.get(), self.difficult.get(), self.game_ball_color, self.game_rackets_color, sep='\n')
		self.destroy()
		game.Game(self.master, self.width, self.height, self.side.get(), self.difficult.get(), self.bcolor, self.rcolor)





class LLabel(Label):
	def __init__(self, master=None, **configs):
		super().__init__(master, font=('Times', 14, 'bold italic'), **configs)
		
class BButton(Button):
	def __init__(self, master=None, **configs):
		super().__init__(master, font=('Times', 10, 'bold'), **configs)

class RRadiobutton(Radiobutton):
	def __init__(self, master, **configs):
		super().__init__(master, font=('Times', 13, 'normal'), **configs)
