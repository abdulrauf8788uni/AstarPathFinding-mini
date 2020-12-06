import pygame
from . import settings
import time
from .myqueue import myPriorityQueue

from .node import Node

# All Fuctions 
def makeGrid():
	node_width = settings.WIDTH // settings.NUM_X
	grid = []
	for row in range(settings.NUM_X):
		grid.append([])
		for node in range(settings.NUM_X):
			new_node = Node(node, row, node_width)
			grid[row].append(new_node)

	return grid

def drawGrid(win, grid):
	for row in grid:
		for node in row:
			node.draw_node(win)

def getClickedNode(grid):
	node_width = settings.WIDTH // settings.NUM_X
	clicked_x, clicked_y =  pygame.mouse.get_pos()
	pos_x = clicked_x // node_width
	pos_y = clicked_y // node_width

	return grid[pos_y][pos_x]

def recalculate_nodes(grid, end_node):
	for row in grid:
		for node in row:
			node.clac_heuristic(end_node.pos())

	for row in grid:
		for node in row:
			node.calc_neighbours(grid)



def Astar(win, grid, start_node, end_node):
	recalculate_nodes(grid, end_node)

	queue = myPriorityQueue()
	explored = []
	best_path_item = ([], float("inf"))
	queue.insert(([start_node], 0), start_node.get_h())


	while not queue.is_empty():

		item, local_f_score = queue.get()
		exploring = item[0][-1]

		exploring.make_explored()
		exploring.draw_node(win)
		pygame.display.update()
		explored.append(exploring)

		children = exploring.neighbours
		for child in children:
			if not child in explored:
				node_list, path_cost = item
				new_path_cost = path_cost + 1

				new_list = list(node_list)

				if child.get_h() == 0:
					for node in new_list:
						if node != start_node and node != end_node:
							node.make_path()
							node.draw_node(win)
							pygame.display.update()
					return 

				f_score = new_path_cost + child.get_h() * 4

				new_list.append(child)
				explored.append(child)
				# print("adding", end=" ")
				# for path in new_list:
				# 	print(path.pos(), end=' ')
				# print("with f score", f_score)
				# print(f"inserting {child.pos()}")
				queue.insert((new_list, new_path_cost), f_score)

	print("No possible path found. ")