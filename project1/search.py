# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
#from util import Queue
#from util import Stack

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    #Stack = LIFO
    open = util.Stack()
    closed = set()

    #Another stack to keep track of directions
    currentpath = util.Stack()
    path = []

    open.push(problem.getStartState())

    while open:
        current = open.pop()
        #print(current)

        if problem.isGoalState(current):
            return path
        
        if current not in closed:
            closed.add(current)
            for child in problem.getSuccessors(current):
                #print(child)

                child_state = child[0]
                #print(child_state)
                child_action = child[1]
                #print(child_action)
                #Push children state and actions (list concatenation since appending returns None)
                open.push(child_state)
                currentpath.push(path + [child_action])

        #Pop corresponding direction after processing children to get ready for popping of next state
        path = currentpath.pop()
        #print(path)
    return []
    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    #Queue = LIFO
    open = util.Queue()
    closed = set()

    #Another queue to keep track of directions
    currentpath = util.Queue()
    path = []

    open.push(problem.getStartState())

    while open:
        current = open.pop()
        #print(current)

        if problem.isGoalState(current):
            return path
        
        if current not in closed:
            closed.add(current)
            for child in problem.getSuccessors(current):
                #print(child)

                child_state = child[0]
                #print(child_state)
                child_action = child[1]
                #print(child_action)
                #Push children state and actions (list concatenation since appending returns None)
                open.push(child_state)
                currentpath.push(path + [child_action])

        #Pop corresponding direction after processing children to get ready for popping of next state
        #print(currentpath.pop())
        path = currentpath.pop()

    return []
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    #PriorityQueue
    open = util.PriorityQueue()
    closed = set()

    #Another queue to keep track of directions
    currentpath = util.PriorityQueue()
    path = []

    open.push(problem.getStartState(), 0)

    while open:
        current = open.pop()
        #print(current)

        if problem.isGoalState(current):
            return path
        
        if current not in closed:
            closed.add(current)
            for child in problem.getSuccessors(current):
                #print(child)

                child_state = child[0]
                #print(child_state)
                child_action = child[1]
                #print(child_action)
                child_cost = problem.getCostOfActions(path + [child_action])
                #Push children state and actions (list concatenation since appending returns None)
                open.push(child_state, child_cost)
                currentpath.push(path + [child_action], child_cost)

        #Pop corresponding direction after processing children to get ready for popping of next state
        path = currentpath.pop()

    return []
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    #PriorityQueue
    open = util.PriorityQueue()
    closed = set()

    #Another queue to keep track of directions
    currentpath = util.PriorityQueue()
    path = []

    open.push(problem.getStartState(), 0)

    while open:
        current = open.pop()
        #print(current)

        if problem.isGoalState(current):
            return path
        
        if current not in closed:
            closed.add(current)
            for child in problem.getSuccessors(current):
                #print(child)

                child_state = child[0]
                #print(child_state)
                child_action = child[1]
                #print(child_action)
                child_cost = problem.getCostOfActions(path + [child_action]) + heuristic(child_state , problem)
                #Push children state and actions (list concatenation since appending returns None)
                open.push(child_state, child_cost)
                currentpath.push(path + [child_action], child_cost)
        
        #Pop corresponding direction after processing children to get ready for popping of next state
        path = currentpath.pop()

    return []
    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
