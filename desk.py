from tkinter import *


class Desk(Canvas):
	def __init__(self, parent=None, width=500, height=300, **configs):
		super().__init__(parent, width=width, height=height, **configs)
		self.width = width
		self.height = height
		self.focus_set()
		self.create_line(self.width / 2, 0, self.width / 2, self.height)

	def score(self):
		self.lp_points = self.create_text(self.width / 4, 15, text='0', font=('Times', 25))
		self.rp_points = self.create_text(self.width / 4 * 3, 15, text='0', font=('Times', 25))

	def set_left_points(self, point):
		self.itemconfigure(self.lp_points, text=str(point))

	def set_right_points(self, point):
		self.itemconfigure(self.rp_points, text=str(point))

