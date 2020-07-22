from tkinter import Canvas


class Racket:
	def __init__(self, can: Canvas, rh, rw, side='l'):
		self.can = can
		self.racket_id = self.create(rh, rw, side)

	def create(self, rh, rw, side='l'):
		self.racket_width = rw
		self.racket_height = rh

		if side == 'l':
			x1 = 2
			x2 = self.racket_width
		elif side == 'r':
			x1 = self.can.width - self.racket_width
			x2 = self.can.width
		y1 = self.can.height / 2 + self.racket_height / 2
		y2 = self.can.height / 2 - self.racket_height / 2

		return self.can.create_rectangle(x1, y1, x2, y2, fill='yellow')

	def move(self, x, y):
		self.can.move(self.racket_id, x, y)

	@property
	def x1(self):
		return self.can.coords(self.racket_id)[0]

	@property
	def x2(self):
		return self.can.coords(self.racket_id)[2]

	@property
	def y1(self):
		return self.can.coords(self.racket_id)[1]

	@property
	def y2(self):
		return self.can.coords(self.racket_id)[3]

	@property
	def y_center(self):
		return self.y1 + self.racket_height / 2
