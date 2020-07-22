from ball import Ball
import game


class Player:
	def __init__(self, game, height=60, width=10, side=0, color='red', speed=5):
		self.game = game
		self.points = 0
		self.height = height
		self.width = width
		self.side = side
		self.color = color
		self.speed = speed
		self.id = self.draw()
		self.moving_up = False
		self.moving_down = False

	def up_press(self, event):
		self.moving_up = True

	def up_release(self, event):
		self.moving_up = False

	def down_press(self, event):
		self.moving_down = True

	def down_release(self, event):
		self.moving_down = False

	def draw(self):
		if not self.side:
			x1 = 2
			x2 = self.width
		else:
			x1 = self.game.desk.width - self.width
			x2 = self.game.desk.width
		y1 = self.game.desk.height / 2 + self.height / 2
		y2 = self.game.desk.height / 2 - self.height / 2

		return self.game.desk.create_rectangle(x1, y1, x2, y2, fill=self.color)

	def move_to_center(self):
		y = self.game.desk.height / 2 - self.y1 - self.height / 2
		self.move(0, y)

	@property
	def x1(self):
		return self.game.desk.coords(self.id)[0]

	@property
	def x2(self):
		return self.game.desk.coords(self.id)[2]

	@property
	def y1(self):
		return self.game.desk.coords(self.id)[1]

	@property
	def y2(self):
		return self.game.desk.coords(self.id)[3]

	def hit_ball(self):
		if not self.side:
			return (self.y1 <= self.game.ball.y2) and (self.y2 >= self.game.ball.y1) and (self.x2 >= self.game.ball.x1)
			# self.ball.move(self.racket2.racket_width - 1, 0)
		else:
			return (self.y1 <= self.game.ball.y2) and (self.y2 >= self.game.ball.y1) and (self.x1 <= self.game.ball.x2)
		# self.ball.move(x - self.racket2.racket_width, 0)

	def ball_on_it_field(self):
		if self.side:
			return self.game.ball.x2 > (self.game.desk.width / 2)
		else:
			return self.game.ball.x1 < (self.game.desk.width / 2)

	@property
	def y_center(self):
		return self.y1 + self.height / 2

	def move(self, x, y):
		self.game.desk.move(self.id, x, y)

	def move_up(self):
		if self.y1 > 0:
			self.move(0, -self.speed)

	def move_down(self):
		if self.y2 < self.game.desk.height:
			self.move(0, self.speed)

