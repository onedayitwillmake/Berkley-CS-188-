# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html
import pacman
import pacmanAgents
from numpy.ma.core import sqrt
from random import random

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", 
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    stack = util.Stack();
    explored = []
    
    def expandSuccessors(aNode):
        """
        Recursively adds successors to the top of the stack, and adds them to the explored set
        If a successor is in the explored set it is ignored.
        Repeats process until goal is reached or stack is empty
        """
        for successor, action, stepCost in problem.getSuccessors(aNode [0]) :
            newNode = (successor, action, aNode, stepCost);    
            # Add to stack if we didn't explore already
            if newNode[0] not in explored:
                if problem.isGoalState(newNode[0]):
                    return newNode;
                stack.push(newNode)
                explored.insert(0, newNode[0])
                    
        # Stack not empty - keep expandingsuccessors
        if stack.isEmpty() is False:
            return expandSuccessors(stack.pop());
        
    
    # Create an initial node, and recursively call expandSuccessors    
    finalNode = expandSuccessors( (problem.getStartState(), None, None, 0 ) );
    

    # Compose directions by going back up the node list
    directions = [];
    itr = finalNode;
    while itr:
        if itr[1] is not None: # First state has no direction
            directions.insert(0, itr[1]);
        itr = itr[2]; # Next one
    
    return  directions;


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    fifoQueue = util.Queue()
    explored = [];
    
    def expandSuccessors( aNode ):
        for successor, action, stepCost in problem.getSuccessors( aNode[0] ):
            newNode = ( successor, action, aNode, stepCost );
            if problem.isGoalState( newNode[0] ):
                return newNode;
                
            if newNode[0] not in explored:
                fifoQueue.push(newNode);
                explored.append(newNode[0]);
                
        # Stack is not empty - keep expanding
        if fifoQueue.isEmpty() is False:
            return expandSuccessors( fifoQueue.pop() );
        
    finalNode = expandSuccessors( (problem.getStartState(), None, None, 0) );
        
    directions = [];
    itr = finalNode;
    while itr:
        if itr[1] is not None: # First state has no direction
            directions.append(itr[1]);
        itr = itr[2]; # Next one
    
    # First node is the goal node, so reverse it so it is the last node
    directions.reverse(); 
    return  directions;

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    
    priorityQueue = util.PriorityQueue()
    explored = [];
    
    def getCumalitiveCost( aNode ):
        itr = aNode;
        cost = 0;
        while itr:
            cost += itr[3]
            itr = itr[2]; # Next one
        return cost;
        
    def isInExploredSet( searchNode ):
        for successor, action, aNode, stepCost in explored:
            if successor == searchNode[0]:
                return (successor, action, aNode, stepCost); 
        return None
        
    def expandSuccessors( aNode ):
        for successor, action, stepCost in problem.getSuccessors( aNode[0] ):
            parentCost = getCumalitiveCost(aNode)
            newNode = ( successor, action, aNode, parentCost+stepCost );
            
            existingNode = isInExploredSet( newNode );
            if existingNode is None:
                priorityQueue.push(newNode, newNode[3] );
                explored.append( newNode );
            elif newNode[3] < existingNode[3]:
                priorityQueue.push( newNode, newNode[3] );
                
            if problem.isGoalState( newNode[0] ):
                return newNode;
            
        # Stack is not empty - keep expanding
        if priorityQueue.isEmpty() is False:
            return expandSuccessors( priorityQueue.pop() );
        
    finalNode = expandSuccessors( (problem.getStartState(), None, None, 0) );
    
    # Starting from the final state, add all the actions that got us here
    directions = [];
    itr = finalNode;
    while itr:
        if itr[1] is not None: # First state has no direction
            directions.append(itr[1]);
        itr = itr[2]; # Next one
    
    # First node is the goal node, so reverse it so it is the last node
    directions.reverse();
    return directions;

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
