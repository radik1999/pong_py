from desk import Desk

class Ball:
	def __init__(self, desk: Desk, width=20, height=20, color='#800040'):
		self.width = width
		self.height = height
		self.desk = desk
		self.color = color
		self.id = self.create()

	def create(self):
		x1 = self.desk.width / 2 - self.width / 2
		x2 = self.desk.width / 2 + self.width / 2
		y1 = self.desk.height / 2 - self.height / 2
		y2 = self.desk.height / 2 + self.height / 2
		return self.desk.create_oval(x1, y1, x2, y2, fill=self.color, outline='white')

	def move_to_center(self):
		x = self.desk.width / 2 - self.x2 + self.width / 2
		y = self.desk.height / 2 - self.y1 - self.height / 2
		self.move(x, y)

	def hit_ceiling(self):
		# if self.y1 < 0:
		# 	self.move(0, 0 - self.y1)
		return self.y1 <= 0

	def hit_flour(self):
		# if self.y2 > self.desk.height:
		# 	self.move(0, self.y2 + self.desk.height)
		return self.y2 >= self.desk.height


	def hit_left_side(self):
		return self.x1 <= 0

	def hit_right_side(self):
		return self.x2 >= self.desk.width

	def move(self, x, y):
		self.desk.move(self.id, x, y)

	@property
	def x1(self):
		return self.desk.coords(self.id)[0]

	@property
	def x2(self):
		return self.desk.coords(self.id)[2]

	@property
	def y1(self):
		return self.desk.coords(self.id)[1]

	@property
	def y2(self):
		return self.desk.coords(self.id)[3]

	@property
	def y_center(self):
		return self.y1 + self.height / 2
