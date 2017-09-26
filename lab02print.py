import util
from util import *
from Node import Node
import copy

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    stack = Stack()
    explored = []

    #implement DFS

    head = Node(problem.getStartState(), list(), None, None)

    stack.push(head)

    while (stack.isEmpty() == False):
        top = stack.pop()
        if (problem.isGoalState(top.currentState) == True):
            return top.action
        explored.append(top.currentState)
        childList = problem.getSuccessors(top.currentState)
        for child in childList:
            childState = child[0]
            if not childState in explored:
                actionList = copy.deepcopy(top.action)
                actionList.append(child[1])
                stack.push(Node(childState, actionList, top, child[2]))

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    queue = Queue()
    explored = []

    #implement BFS

    head = Node(problem.getStartState(), list(), None, None)

    queue.push(head)

    while (queue.isEmpty() == False):
        top = queue.pop()
        if (problem.isGoalState(top.currentState) == True):
            return top.action
        explored.append(top.currentState)
        childList = problem.getSuccessors(top.currentState)
        for child in childList:
            childState = child[0]
            if not childState in explored:
                actionList = copy.deepcopy(top.action)
                actionList.append(child[1])
                queue.push(Node(childState, actionList, top, child[2]))

    util.raiseNotDefined()
