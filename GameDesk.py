import time
from tkinter import *
from ball import Ball
from racket import Racket
from random import choice
from scoreboard import ScoreBoard

class Desk(Canvas):
	def __init__(self, parent=None, h=None, w=None, **configs):
		super().__init__(parent, height=h, width=w, bd=0, **configs)
		self.height = h
		self.width = w
		self.pack(expand=YES, fill=BOTH)
		self.score_board = ScoreBoard()
		self.draw_elements()
		self.dr_l = [(4, 4), (4, -4), (5, 3), (5, -3), (6, 2), (6, -2), (7, 1), (7, -1)]
		self.dr_r = [(-4, 4), (-4, -4), (-5, 3), (-5, -3), (-6, 2), (-6, -2), (-7, 1), (-7, -1)]
		self.upf = False
		self.downf = False
		self.focus_set()
		self.bind('<KeyPress>', self.start)
		self.bind('<Up>', self.up_pressed)
		self.bind('<KeyRelease-Up>', self.up_released)
		self.bind('<Down>', self.down_pressed)
		self.bind('<KeyRelease-Down>', self.down_released)

	def draw_elements(self):
		self.racket1 = Racket(self, 60, 10, 'l')
		self.racket2 = Racket(self, 60, 10, 'r')
		self.create_line(self.width / 2, 0, self.width / 2, self.height)
		self.score1 = self.create_text(self.width/4, 20, text='0', font=('Verdana', 25, 'normal'))
		self.score2 = self.create_text(self.width/4*3, 20, text='0', font=('Verdana', 25, 'normal'))
		self.ball = Ball(self)
		self.text = self.create_text(self.width/2, self.height/2, text='Press any button to start', font=('Verdana', 25, 'normal'),
									 fill='red')

	def start(self, event=None):
		self.delete(self.text)
		self.move_ball()

	def up_pressed(self, event):
		self.upf = True

	def up_released(self, event: Event):
		self.upf = False

	def down_pressed(self, event):
		self.downf = True

	def down_released(self, event):
		self.downf = False

	def redraw_ball(self):
		x = self.width/2 - self.ball.x2 + self.ball.width / 2
		y = self.height/2 - self.ball.y1 - self.ball.height/2
		self.ball.move(x, y)
		y = self.height/2 - self.racket2.y1 - self.racket2.racket_height/2
		self.racket2.move(0, y)
		y = self.height/2 - self.racket1.y1 - self.racket1.racket_height/2
		self.racket1.move(0, y)


	def draw_racket(self, rh, rw, side=''):
		self.racket_width = rw
		self.racket_height = rh

		if side == 'l':
			self.rx_from = 2
			self.rx_to = self.racket_width
		elif side == 'r':
			self.rx_from = self.width - self.racket_width
			self.rx_to = self.width
		self.ry_from = self.height/2 + self.racket_height/2
		self.ry_to = self.height/2 - self.racket_height/2

		rid = self.create_rectangle(self.rx_from, self.ry_from, self.rx_to, self.ry_to, fill='yellow')
		return rid

	def wait(self, t):
		if t:
			self.after(1000, self.wait, t-1)
		else:
			self.move_ball()

	def create_report(self, player):
		self.score_board = ScoreBoard()
		self.itemconfigure(self.score1, text=0)
		self.itemconfigure(self.score2, text=0)

		log = Toplevel(self.master)
		log.geometry('+550+300')
		Label(log, text=f'{player} won', font=('Verdana', 25, 'normal')).pack(side=TOP)
		Button(log, text='Quit', font=('Verdana', 10, 'normal'), command=lambda: log.destroy() or self.master.quit()).pack(side=LEFT)
		Button(log, text='Start New', font=('Verdana', 10, 'normal'), command=lambda: log.destroy() or self.start()).pack(side=RIGHT)
		log.focus_set()
		log.grab_set()
		log.wait_window()


	def move_ball(self, x=-8, y=0):
		# ricochet top and bot
		drct1 = choice(self.dr_l)
		drct2 = choice(self.dr_r)
		if (self.ball.y2 > self.height) or (self.ball.y1 < 0):
			y = -y

		# real player racket logic
		direction = [1, -1]
		if ((self.racket1.y1 <= self.ball.y2) and
				(self.racket1.y2 >= self.ball.y1)):
			if self.racket1.x2 >= self.ball.x1:
				x = -x
				self.ball.move(self.racket2.racket_width - 1, 0)
				x = drct1[0]
				y = drct1[1]
				print(x, y)

		# angel ricochet
		# if self.racket1.x2 > self.ball.x1:
		# 	print(x, y)
		# 	x = -x
		# 	y = -y

		if self.ball.x1 <= 0:
			if self.score_board.second_won():
				self.create_report('Second')
			self.itemconfigure(self.score2, text=self.score_board.player2)
			self.redraw_ball()
			self.wait(1)
			return 0

		if self.ball.x2 > self.width/2:
			# x = -x
			if (self.ball.y_center > self.racket2.y_center) and (self.racket2.y2 < self.height):
				self.racket2.move(0, 3.5)
			if (self.ball.y_center < self.racket2.y_center) and (self.racket2.y1 > 0):
				self.racket2.move(0, -3.5)

		if ((self.ball.y2 >= self.racket2.y1) and
				(self.racket2.y2 >= self.ball.y1)):
			if self.racket2.x1 <= self.ball.x2:
				x = -x
				self.ball.move(x - self.racket2.racket_width, 0)
				x = drct2[0]
				y = drct2[1]
				print(x, y)
		#angel ricochet
		# elif self.racket2.x1 < self.ball.x2:
		# 	x = -x
		# 	y = -y
		# 	self.ball.move(x - self.racket2.racket_width, 0)

		if self.ball.x2 >= self.width:
			if self.score_board.first_won():
				self.create_report('First')
			self.itemconfigure(self.score1, text=self.score_board.player1)
			self.redraw_ball()
			self.wait(1)
			return 0

		self.ball.move(x, y)
		if self.upf:
			if self.racket1.y1 > 0:
				self.racket1.move(0, -5)
		if self.downf:
			if self.racket1.y2 < self.height:
				self.racket1.move(0, 5)

		self.after(14, self.move_ball, x, y)

