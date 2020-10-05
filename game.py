import random
from tkinter import *

from gameType import GameType
from startscreen import StartScreen
from prototype import GamePrototype


class Game(GamePrototype):
	def __init__(self, master=None, width=500, height=300, player_side=False, difficult=2, ball_color='blue', rackets_color='red'):
		super().__init__(master, player_side, difficult, ball_color, rackets_color, width, height, 20, 20, 10, 60)
		self.desk.score()
		self.desk.pack()
		self.players = {'right': self.player1 if self.player1.side else self.player2,
						'left': self.player1 if not self.player1.side else self.player2}
		self.start_text = self.desk.create_text(self.desk.width / 2, self.desk.height / 2,
												text='Press "SPACE" button to start',
												font=('Verdana', 20, 'normal'),
												fill='black')
		self.left_ricochet = [(4, 4), (4, -4), (5, 3), (5, -3), (6, 2), (6, -2), (7, 1), (7, -1)]
		self.right_ricochet = [(-4, 4), (-4, -4), (-5, 3), (-5, -3), (-6, 2), (-6, -2), (-7, 1), (-7, -1)]
		self.desk.bind('<space>', self.start)
		self.desk.bind('<Up>', self.player1.up_press)
		self.desk.bind('<KeyRelease-Up>', self.player1.up_release)
		self.desk.bind('<Down>', self.player1.down_press)
		self.desk.bind('<KeyRelease-Down>', self.player1.down_release)
		if player_side is None:
			self.desk.bind('<Key-w>', self.player2.up_press)
			self.desk.bind('<KeyRelease-w>', self.player2.up_release)
			self.desk.bind('<Key-s>', self.player2.down_press)
			self.desk.bind('<KeyRelease-s>', self.player2.down_release)


	def start(self, event=None):
		self.desk.delete(self.start_text)
		x = random.choice((8, -8))
		self.loop(x)

	def end_report(self, plr):
		report = Toplevel(self.master)
		side = 'right' if plr.side else 'left'
		Label(report, text=f'{side} player has won', font=('Verdana', 25, 'normal')).pack()
		Button(report, text='Main menu', font=('Verdana', 10, 'normal'), command=lambda: report.destroy() or self.main_menu()).pack(side=LEFT)
		Button(report, text='New game', font=('Verdana', 10, 'normal'), command=lambda: report.destroy() or self.new_game()).pack(side=RIGHT)
		report.focus_set()
		report.grab_set()
		report.wait_window()

	def main_menu(self):
		self.desk.destroy()
		GameType(self.master, self.width, self.height, self.ball.color, self.player1.color)

	def new_game(self):
		self.desk.destroy()
		Game(self.master, self.width, self.height, self.player_side, self.difficult, self.ball.color, self.player1.color)

	def new_start(self, plr, wait=2):
		self.ball.move_to_center()
		self.player1.move_to_center()
		self.player2.move_to_center()
		if plr.points == 10:
			self.end_report(plr)
			return 0
		if wait:
			self.desk.after(1000, self.new_start, plr, wait - 1)
		else:
			self.start()

	def loop(self, x=-8, y=0):
		self.ball.move(x, y)

		if self.ball.hit_left_side():
			plr = self.players['right']
			plr.points += 1
			self.desk.set_right_points(plr.points)
			return self.new_start(plr, 1)

		if self.ball.hit_right_side():
			plr = self.players['left']
			plr.points += 1
			self.desk.set_left_points(plr.points)
			return self.new_start(plr, 1)

		if self.player1.hit_ball():
			if self.player1.side:
				x, y = random.choice(self.right_ricochet)
			else:
				x, y = random.choice(self.left_ricochet)

		if self.player2.hit_ball():
			if self.player2.side:
				x, y = random.choice(self.right_ricochet)
			else:
				x, y = random.choice(self.left_ricochet)

		if self.ball.hit_ceiling() or self.ball.hit_flour():
			y = -y

		self.move_racket(player=self.player1)

		if self.player_side is None:
			self.move_racket(player=self.player2)
		else:
			self.auto_move(player=self.player2)


		# if self.player1.moving_up:
		# 	self.player1.move_up()
		# if self.player1.moving_down:
		# 	self.player1.move_down()

		# if self.player2.moving_up:
		# 	self.player2.move_up()
		# if self.player2.moving_down:
		# 	self.player2.move_down()

		self.desk.after(15, self.loop, x, y)

	def move_racket(self, player):
		if player.moving_up:
			player.move_up()
		if player.moving_down:
			player.move_down()

	def auto_move(self, player):
		if player.ball_on_it_field():
			if self.ball.y_center > player.y_center:
				player.move_down()
			if self.ball.y_center < player.y_center:
				player.move_up()
