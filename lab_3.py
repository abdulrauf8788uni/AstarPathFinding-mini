"""
Lab Task: 

For this lab you will be implementing A* (A Star Search) on a graph.
The picture of the graph can be found in assets directory.

For this lab you are provided with two helper classes.
One is for making a graph and the other one in an interface for Priority Queues.
You may open then these file, once opened you'll see descriptions for each function defined
and a testing code for the class in the main body. Kindly go through them to get comfortable 
with the functions

MAIN TASKS:

    1- Modify graph.py to have the ability to store heuristics
    2- Create a funciton 'get_h' in graph.py to get heuristic for a node : input will be a Node and output will be heuristic 
    3- Create the graph in graph.py to and check all the functions
    4- Replicate the graph in 'lab_3.py'
    5- Implement A* function 

Your function should print the shortest path along with the cost of that path. 
A sample output is provided in the assests directory.
"""

# importing helper classes
from graph import Graph
from queue import PriorityQueue

def a_star_search(graph, start_node, goal_node):

    # queue = PriorityQueue()
    # queue.insert(start_node, 0)
    # explored = []

    # best_path = ("", 9999)
    # while not queue.is_empty():
    #     path_cost, path = queue.remove()

    #     if path[-1] == goal_node and path[0] == start_node:
    #         if path_cost < best_path[1]:
    #             best_path = (path, path_cost)
    #     explored.append(path[-1])
    #     children = graph.neighbours(path[-1])
    #     if children:
    #         for child in children:
    #             if not child in explored:
    #                 area_cost = path_cost + graph.get_cost(path[-1], child)
    #                 newpath = path + child
    #                 queue.insert(newpath, area_cost)
    

    # print("Shrotest Path: ", ",".join(best_path[0]))
    # print("Cost: ", best_path[1])

    queue = PriorityQueue()
    explored = []
    best_path_item = ("", float("inf"))
    queue.insert((start_node, 0), graph.get_h(start_node))

    # queue = [((path, path_cost), f_cost)]
    # f_cost = path_cost + heuristic 

    while not queue.is_empty():
        local_cost, prior_item = queue.remove()
        path, path_cost = prior_item  # prior item: (path, path_cost)

        children = graph.neighbours(path[-1])
        explored.append(path[-1])
        if children:
            for child in children:
                new_path = path + child
                new_path_cost = path_cost + graph.get_cost(path[-1], child)
                f_cost = new_path_cost + graph.get_h(child)
                prior_item = (new_path, new_path_cost)
                queue.insert(prior_item, f_cost)
        else:
            if local_cost < best_path_item[1]:
                best_path_item = (path, local_cost)

    print("Best Path: ", end=" ")
    print(" -> ".join(best_path_item[0]))
    print("Cost: ",best_path_item[-1])



if __name__ == "__main__":
    
    graph = Graph()

    # setting up nodes and neighbours
    graph.edges = {
        "S": set(['A', 'D']),
        "A": set(['B', 'C']),
        "B": set(['C', 'E']),
        "C": set(['G']),
        "D": set(['B', 'E']),
        "E": set(['G']),
        "G": None

    }

    graph.weights = {
        'SA': 3, 'SD':2,
        'AB': 5, 'AC':10,
        'BC': 2, 'BE':1,
        'CG': 4, 
        'DB': 1, 'DE': 4,
        'EG': 3,
    }

    graph.heuristics = {
        "S": 7,
        "A": 9,
        "B": 4,
        "C": 2,
        "D": 5, 
        "E": 3,
        "G": 0,
    }

    a_star_search(graph, 'S', 'G') 