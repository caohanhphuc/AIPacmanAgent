class Node:
	def __init__(self, currentState, action, parent):
		self.currentState = currentState
		self.parent = parent
		self.action = action
		self.stepCost = 0
		self.pathCost = 0
