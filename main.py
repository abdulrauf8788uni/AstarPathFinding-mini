import pygame
from mygame.functions import makeGrid, drawGrid, getClickedNode, Astar
from mygame import settings

# Pygame settings

WIN = pygame.display.set_mode(settings.SCREEN)
pygame.display.set_caption(settings.CAPTION)


# Local variables
run = True
started = False
grid = makeGrid()

start_node = None
end_node = None

while run:

	WIN.fill(settings.BLACK)
	drawGrid(WIN, grid)


	for event in pygame.event.get():
		# Exiting fuction 
		if event.type == pygame.QUIT:
			run = False
			print(f"Exiting '{settings.CAPTION}'")
		# Reset screen
		if not started:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					grid = makeGrid()
					start_node = None
					end_node = None

				if event.key == pygame.K_SPACE:
					started = True

			# Mouse left click functionality 
			if pygame.mouse.get_pressed()[0]:
				# Start node, end node and barrier node logic
				clicked_node = getClickedNode(grid)
				if not start_node and not end_node:
					start_node = clicked_node
					start_node.make_start()
				elif not end_node and clicked_node != start_node:
					end_node = clicked_node
					end_node.make_end()
				elif clicked_node != start_node and clicked_node != end_node:
					clicked_node.make_barrier()

			# Mouse right click functionality
			elif pygame.mouse.get_pressed()[2]:
				clicked_node = getClickedNode(grid)
				if clicked_node == end_node:
					end_node = None

				elif clicked_node == start_node:
					if end_node:
						end_node.make_start()
						start_node = end_node
						end_node = None
				clicked_node.reset() 
	if started:
		print("Running A* algorithm.")
		Astar(WIN, grid, start_node, end_node)
		started = False		

	pygame.display.update()

# pygame.quit()