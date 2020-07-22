from desk import Desk
from ball import Ball
from player import Player


class GamePrototype:
	def __init__(self, master=None, player_side=False, difficult=2, ball_color='blue', rackets_color='red', width=200,
				 height=110, ball_height=15, ball_width=15, racket_width=15, racket_height=30):
		self.master = master
		self.difficult = difficult
		self.player_side = player_side
		self.width = width
		self.height = height
		if difficult == 1:
			player_speed = 5
			computer_speed = 3
		elif difficult == 2:
			player_speed = 4
			computer_speed = 3.5
		elif difficult == 3:
			player_speed = 3
			computer_speed = 4
		else:
			player_speed = 4
			computer_speed = 4

		if player_side is None:
			player1_side = False
			player2_side = True
		else:
			player1_side = player_side
			player2_side = not player_side
		self.desk = Desk(master, width=width, height=height)
		self.player1 = Player(self, width=racket_width, height=racket_height, side=player1_side, speed=player_speed, color=rackets_color)
		self.player2 = Player(self, width=racket_width, height=racket_height, side=player2_side, speed=computer_speed, color=rackets_color)
		self.ball = Ball(self.desk, ball_width, ball_height, ball_color)
