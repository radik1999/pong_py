

class ScoreBoard:
	def __init__(self):
		self.player1 = 0
		self.player2 = 0
		self.max_score = 3

	def first_won(self):
		self.player1 += 1
		if self.player1 == self.max_score:
			return True
		return False

	def second_won(self):
		self.player2 += 1
		if self.player2 == self.max_score:
			return True
		return False
