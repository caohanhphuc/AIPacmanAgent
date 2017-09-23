class Node:
	def __init__(self, currentState, parent):
        self.currentState = currentState
        self.parent = parent
        self.action = []
        self.stepCost = 0
        self.pathCost = 0
