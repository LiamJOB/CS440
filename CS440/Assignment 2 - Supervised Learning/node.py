import random
import math
from pprint import *
from decimal import *
from classes import *
from decimal import *
from binaryHeap import *
class Node(object):
	def __init__(self, cell):
		self.cell = cell
		self.parent = None
		self.gCost = 0
		self.fCost = 0
		self.neighbours = []

def heuristicVal(s, start, goal):
	sx = s[0]
	sy = s[1]
	startx = start[0]
	starty = start[1]
	goalx = goal[0]
	goaly = goal[1]
	return Decimal(math.sqrt(2) * min(abs(sx-goalx), abs(sy-goaly)) + max(abs(sx-goalx), abs(sy-goaly)) - min(abs(sx-goalx), abs(sy-goaly)))


def generateNeighbours(node1, mapp, rows, columns, algo, w):
	cell = node1.cell
	mapMatrix = mapp.mapMatrix
	start = mapp.start
	goal = mapp.goal
	listt = []
	w = Decimal(w)
	# if mapMatrix[cell.row + 1][cell.col].type == 0 or mapMatrix[cell.row + 1][cell.col + 1].type == 0:
		# print "BLOCKED CELL"
	if cell.row - 1 >= 0 and mapMatrix[cell.row - 1][cell.col].type != 0:
		cellNeighbor = mapMatrix[cell.row - 1][cell.col]
		nodeNeighbor = Node(cellNeighbor)
		nodeNeighbor.parent = node1
		nodeNeighbor.gCost = cost(cell, cellNeighbor) + node1.gCost
		if algo == 'U':
			nodeNeighbor.fCost = nodeNeighbor.gCost
		if algo == 'A':
			w = 1
			s = [cell.row - 1, cell.col]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + Decimal(w*h)
		if algo == 'W':
			s = [cell.row - 1, cell.col]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + Decimal(w*h)
		listt.append(nodeNeighbor)
		if node1.parent is not None:
			if node1.parent.cell.row == nodeNeighbor.cell.row and node1.parent.cell.col == nodeNeighbor.cell.col:
				listt.remove(nodeNeighbor)
	if cell.row + 1 < rows and mapMatrix[cell.row + 1][cell.col].type != 0:
		cellNeighbor = mapMatrix[cell.row + 1][cell.col]
		nodeNeighbor = Node(cellNeighbor)
		nodeNeighbor.parent = node1
		nodeNeighbor.gCost = cost(cell, cellNeighbor) + node1.gCost
		if algo == 'U':
			nodeNeighbor.fCost = nodeNeighbor.gCost
		if algo == 'A':
			w = 1
			s = [cell.row + 1, cell.col]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + Decimal(w*h)
		if algo == 'W':
			s = [cell.row + 1, cell.col]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + Decimal(w*h)
		listt.append(nodeNeighbor)
		if node1.parent is not None:
			if node1.parent.cell.row == nodeNeighbor.cell.row and node1.parent.cell.col == nodeNeighbor.cell.col:
				listt.remove(nodeNeighbor)
	if cell.col - 1 >= 0 and mapMatrix[cell.row][cell.col - 1].type != 0:
		cellNeighbor = mapMatrix[cell.row][cell.col - 1]
		nodeNeighbor = Node(cellNeighbor)
		nodeNeighbor.parent = node1
		nodeNeighbor.gCost = cost(cell, cellNeighbor) + node1.gCost
		if algo == 'U':
			nodeNeighbor.fCost = nodeNeighbor.gCost
		if algo == 'A':
			w = 1
			s = [cell.row, cell.col-1]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + Decimal(w*h)
		if algo == 'W':
			s = [cell.row, cell.col -1]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + Decimal(w*h)
		listt.append(nodeNeighbor)
		if node1.parent is not None:
			if node1.parent.cell.row == nodeNeighbor.cell.row and node1.parent.cell.col == nodeNeighbor.cell.col:
				listt.remove(nodeNeighbor)
	if cell.col + 1 < columns and mapMatrix[cell.row][cell.col + 1].type != 0:
		cellNeighbor = mapMatrix[cell.row][cell.col + 1]
		nodeNeighbor = Node(cellNeighbor)
		nodeNeighbor.parent = node1
		nodeNeighbor.gCost = cost(cell, cellNeighbor) + node1.gCost
		if algo == 'U':
			nodeNeighbor.fCost = nodeNeighbor.gCost
		if algo == 'A':
			w = 1
			s = [cell.row, cell.col+1]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + Decimal(w*h)
		if algo == 'W':
			s = [cell.row, cell.col+1]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + Decimal(w*h)
		listt.append(nodeNeighbor)
		if node1.parent is not None:
			if node1.parent.cell.row == nodeNeighbor.cell.row and node1.parent.cell.col == nodeNeighbor.cell.col:
				listt.remove(nodeNeighbor)
	if cell.row - 1  >= 0 and cell.col - 1 >= 0 and mapMatrix[cell.row - 1][cell.col - 1].type != 0:
		cellNeighbor = mapMatrix[cell.row - 1][cell.col - 1]
		nodeNeighbor = Node(cellNeighbor)
		nodeNeighbor.parent = node1
		nodeNeighbor.gCost = cost(cell, cellNeighbor) + node1.gCost
		if algo == 'U':
			nodeNeighbor.fCost = nodeNeighbor.gCost
		if algo == 'A':
			w = 1
			s = [cell.row -1, cell.col-1]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + Decimal(w*h)
		if algo == 'W':
			s = [cell.row-1, cell.col-1]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + Decimal(w*h)
		listt.append(nodeNeighbor)
		if node1.parent is not None:
			if node1.parent.cell.row == nodeNeighbor.cell.row and node1.parent.cell.col == nodeNeighbor.cell.col:
				listt.remove(nodeNeighbor)
	if cell.row + 1  < rows and cell.col - 1 >= 0 and mapMatrix[cell.row + 1][cell.col - 1].type != 0:
		cellNeighbor = mapMatrix[cell.row + 1][cell.col - 1]
		nodeNeighbor = Node(cellNeighbor)
		nodeNeighbor.parent = node1
		nodeNeighbor.gCost = cost(cell, cellNeighbor) + node1.gCost
		if algo == 'U':
			nodeNeighbor.fCost = nodeNeighbor.gCost
		if algo == 'A':
			w = 1
			s = [cell.row + 1, cell.col-1]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + Decimal(w*h)
		if algo == 'W':
			s = [cell.row + 1, cell.col-1]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + Decimal(w*h)
		listt.append(nodeNeighbor)
		if node1.parent is not None:
			if node1.parent.cell.row == nodeNeighbor.cell.row and node1.parent.cell.col == nodeNeighbor.cell.col:
				listt.remove(nodeNeighbor)
	if cell.row - 1  >= 0 and cell.col + 1 < columns and mapMatrix[cell.row - 1][cell.col + 1].type != 0:
		cellNeighbor = mapMatrix[cell.row - 1][cell.col + 1]
		nodeNeighbor = Node(cellNeighbor)
		nodeNeighbor.parent = node1
		nodeNeighbor.gCost = cost(cell, cellNeighbor) + node1.gCost
		if algo == 'U':
			nodeNeighbor.fCost = nodeNeighbor.gCost
		if algo == 'A':
			w = 1
			s = [cell.row-1, cell.col+1]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + w*h
		if algo == 'W':
			s = [cell.row-1, cell.col+1]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + w*h
		listt.append(nodeNeighbor)
		if node1.parent is not None:
			if node1.parent.cell.row == nodeNeighbor.cell.row and node1.parent.cell.col == nodeNeighbor.cell.col:
				listt.remove(nodeNeighbor)
	if cell.row + 1  < rows and cell.col + 1 < columns and mapMatrix[cell.row + 1][cell.col + 1].type != 0:
		cellNeighbor = mapMatrix[cell.row + 1][cell.col + 1]
		nodeNeighbor = Node(cellNeighbor)
		nodeNeighbor.parent = node1
		nodeNeighbor.gCost = cost(cell, cellNeighbor) + node1.gCost
		if algo == 'U':
			nodeNeighbor.fCost = nodeNeighbor.gCost
		if algo == 'A':
			w = 1
			s = [cell.row + 1, cell.col+1]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + Decimal(w*h)
		if algo == 'W':
			s = [cell.row + 1, cell.col+1]
			h = heuristicVal(s, start, goal)
			nodeNeighbor.fCost = Decimal(nodeNeighbor.gCost) + Decimal(w*h)
		listt.append(nodeNeighbor)
		if node1.parent is not None:
			if node1.parent.cell.row == nodeNeighbor.cell.row and node1.parent.cell.col == nodeNeighbor.cell.col:
				listt.remove(nodeNeighbor)
	return listt

# Search element in heap
def search(hp, nd):
	arr = []
	if len(hp) == 0:
		return False
	newnd = nd
	while len(hp)>0:
		newnd = hp.pop()
		arr.append(newnd)
		if ((newnd.cell.row == nd.cell.row and newnd.cell.col == nd.cell.col) or newnd.fCost > nd.fCost):
			break
	if (newnd.cell.row == nd.cell.row and newnd.cell.col == nd.cell.col):
		ret = True
	else:
		ret = False
	for a in arr:
		hp.push(a)
	return ret

# def heuristicPath(mapp, algo, rows, columns, w):
# 	mapMatrix = mapp.mapMatrix
# 	start = mapp.start
# 	goal = mapp.goal

# 	print "START:", start
# 	print "GOAL:", goal
# 	startCell = mapMatrix[start[0]][start[1]]
# 	startNode = Node(startCell)
# 	#WE WILL USE BETTER IMPLEMENTATION
# 	closedList = Heap()
# 	openList = Heap()
# 	openList.push(startNode)

# 	while len(openList) >0:
# 		current = openList.pop()
# 		print current.cell.row, ",", current.cell.col
# 		current.neighbours = generateNeighbours(current, mapp, rows, columns, algo, w)
# 		if current.cell.row == goal[0] and current.cell.col == goal[1]:
# 			return reconstructPath(current)

# 		closedList.push(current)

# 		for neighbour in current.neighbours:

# 			if neighbour.cell.row == goal[0] and neighbour.cell.col == goal[1]:
# 				return reconstructPath(current)

# 			if search(closedList, neighbour) == True:
# 				# print "IGNORE NEIGHBOUR"
# 				continue
# 			if search(openList, neighbour) == False:
# 				openList.push(neighbour)

# 			tentativeGCost = current.gCost + cost(current.cell, neighbour.cell)
# 			if tentativeGCost >= neighbour.gCost:
# 				# print "WORKING HWEHJSHDFJLJSFKL:JFKSFKLFJKSJMNJFHOIJSIEHJKLDJSKKZLJFDSKFHSIOJJHDS:"
# 				continue
# 			neighbour.gCost = tentativeGCost
# 			if algo == 'U':
# 				neighbour.fCost = neighbour.gCost
# 			if algo == 'A':
# 				s = [neighbour.cell.row, neighbour.cell.col]
# 				neighbour.fCost = neighbour.gCost + heuristicVal(s, start, goal)
# 		# print "WORKING"
# 	return "failure"

def heuristicPath(mapp, algo, rows, columns, w):

	openSet = Heap()

	start = mapp.start
	goal = mapp.goal
	mapMatrix = mapp.mapMatrix

	print "START:", start
	print "GOAL:", goal
	startNode = Node(mapMatrix[start[0]][start[1]])
	openSet.push(startNode)

	iterat = 0
	while len(openSet) > 0:
		if iterat > 19200:
			break
		currentNode = openSet.pop()
		iterat = iterat + 1
		print currentNode.cell.row, ",", currentNode.cell.col, ",", iterat
		if currentNode.cell.row == goal[0] and currentNode.cell.col == goal[1]:
			return reconstructPath(currentNode)
		
		currentNode.cell.explored = True
		currentNode.neighbours = generateNeighbours(currentNode, mapp, rows, columns,algo, w)
		for neighbour in currentNode.neighbours:
			if neighbour.cell.row == goal[0] and neighbour.cell.col == goal[1]:
				return reconstructPath(neighbour)
			if neighbour.cell.explored == True:
				continue
			# if search(openSet, neighbour) == False:
			openSet.push(neighbour)

			tentativeGCost = currentNode.gCost + cost(currentNode.cell, neighbour.cell)
			if tentativeGCost >= neighbour.gCost:
				continue

			neighbour.parent = currentNode
			neighbour.gCost = tentativeGCost
			if algo == 'U':
				neighbour.fCost = neighbour.gCost
			if algo == 'A' or algo == 'W':
				s = [neighbour.cell.row, neighbour.cell.col]
				neighbour.fCost = neighbour.gCost + Decimal(w) *heuristicVal5(s, start,goal)

	return "FAILURE"

#
def heuristicVal1(s, start, goal):
	sx = s[0]
	sy = s[1]
	startx = start[0]
	goalx = goal[0]
	starty = start[1]
	goaly = goal[1]
	dx = Decimal(abs(sx - goalx))
	dy = Decimal(abs(sy - goaly))	
	dxx = Decimal(abs(startx - goalx))
	dxy = Decimal(abs(starty - goaly))
	cross = Decimal(abs(dx*dyy - dxx*dy))
	return cross


#DIAGONAL DISTANCE -- CHEBYSHEV DISTANCE
def heuristicVal2(s, start, goal):
	sx = s[0]
	sy = s[1]
	startx = start[0]
	goalx = goal[0]
	starty = start[1]
	goaly = goal[1]
	dx = Decimal(abs(sx - goalx))
	dy = Decimal(abs(sy - goaly))
	return Decimal((dx + dy) - min(dx, dy))

#EUCLIDEAN DISTANCE
def heuristicVal3(s, start, goal):
	sx = s[0]
	sy = s[1]
	startx = start[0]
	goalx = goal[0]
	starty = start[1]
	goaly = goal[1]
	dx = Decimal(abs(sx - goalx))
	dy = Decimal(abs(sy - goaly))
	return Decimal(math.sqrt(dx*dx + dy*dy))

def heuristicVal4(s, start, goal):
	sx = s[0]
	sy = s[1]
	startx = start[0]
	goalx = goal[0]
	starty = start[1]
	goaly = goal[1]
	dx = Decimal(abs(sx - goalx))
	dy = Decimal(abs(sy - goaly))
	dxx = Decimal(abs(startx - goalx))
	dxy = Decimal(abs(starty - goaly))
	if random.random() < 0.2:
		return Decimal(dx + dy)
	if random.random() < 0.1875:
		return Decimal(math.sqrt(dx*dx + dy*dy)*math.sqrt(2) + math.sqrt(8)*math.sqrt(dxx*dxx +dyy*dyy))
	return Decimal(math.sqrt(dx*dx + dy*dy)*math.sqrt(2))

def heuristicVal5(s, start, goal):
	sx = s[0]
	sy = s[1]
	startx = start[0]
	goalx = goal[0]
	starty = start[1]
	goaly = goal[1]
	dx = Decimal(abs(sx - goalx))
	dy = Decimal(abs(sy - goaly))	
	dxx = Decimal(abs(startx - goalx))
	dxy = Decimal(abs(starty - goaly))
	cross = Decimal(abs(dx*dyy - dxx*dy))
	return cross

# def sequentialHeuristic(mapp, algo, rows, columns, w):
# 	mapMatrix = mapp.mapMatrix
# 	start = mapp.start
# 	goal = mapp.goal

# 	startNode = Node(mapMatrix[start[0]][start[1]])
# 	goalNode = Node(mapMatrix[goal[0]][goal[1]])

# 	startNode.gCost = 0
# 	goalNode.gCost = float("inf")

# 	openSet = Heap()
# 	closedSet = Heap()
# 	openSet.push(startNode)

# 	while(len(openSet) > 0):




def reconstructPath(currentNode):
	pathh = []
	currPoint = currentNode
	while currentNode.parent != None:
		celll = currentNode.cell
		ro = celll.row
		co = celll.col
		path = [ro,co]
		pathh.append(path)
		currentNode = currentNode.parent
	return pathh

