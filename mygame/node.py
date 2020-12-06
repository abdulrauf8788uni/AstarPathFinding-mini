import pygame
from . import settings

# Node class

class Node:
	def __init__(self, x, y, width):
		self.x = x
		self.y = y
		self.x_pos = self.x * width
		self.y_pos = self.y * width
		self.width = width
		self.color = settings.SILVER
		self.heuristic = float("inf")
		self.neighbours = []



	def pos(self):
		return (self.x, self.y)

	def get_h(self):
		return self.heuristic 

	def clac_heuristic(self, p2):
		p1x, p1y = self.x, self.y
		p2x, p2y = p2

		self.heuristic =  abs(p2x - p1x) + abs(p2y - p1y)

	def calc_neighbours(self, grid):

		if self.x > 0: # LEFT
			if not grid[self.y][self.x - 1].is_barrier():
				self.neighbours.append(grid[self.y][self.x - 1])

		if self.x < settings.NUM_X - 1:
			if not grid[self.y][self.x + 1].is_barrier():
				self.neighbours.append(grid[self.y][self.x + 1])

		if self.y > 0:
			if not grid[self.y - 1][self.x].is_barrier():
				self.neighbours.append(grid[self.y - 1][self.x])

		if self.y < settings.NUM_X - 1:
			if not grid[self.y + 1][self.x].is_barrier():
				self.neighbours.append(grid[self.y + 1][self.x])

	def draw_node(self, win):
		pygame.draw.rect(win, self.color, (self.x_pos , self.y_pos, self.width, self.width)) 

	# Is fuctions

	def is_barrier(self):
		return self.color == settings.BLACK

	def is_start(self):
		return self.color == settings.GREEN
	
	def is_end(self):
		return self.color == settings.RED

	def is_path(self):
		return self.color == settings.YELLOW

	def is_explored(self):
		return self.color == settings.SKIN
	# Setters 

	def make_barrier(self):
		self.color = settings.BLACK

	def reset(self):
		self.color = settings.SILVER

	def make_start(self):
		self.color = settings.GREEN

	def make_end(self):
		self.color = settings.RED

	def make_path(self):
		self.color = settings.YELLOW

	def make_explored(self):
		self.color = settings.DARK_SILVER

	def __str__(self):
		return f"Node at ({self.x}, {self.y})"
