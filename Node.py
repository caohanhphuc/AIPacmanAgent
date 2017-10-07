class Node:
	def __init__(self, currentState, action, parent, stepCost, pathCost):
		self.currentState = currentState
		self.action = action
		self.parent = parent
		self.stepCost = stepCost
		self.pathCost = pathCost
