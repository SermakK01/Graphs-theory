import json
import numpy as np

class Graph:
    edges = []
    number_of_vertexes = -1
    starting_vertex = -1

#Bellmana-Forda algorithm
def BellmanFord(graph):
    dist = [float(np.inf)] * graph.number_of_vertexes
    dist[graph.starting_vertex] = 0

    for i in range(0, graph.number_of_vertexes - 1):
        change = False
        for edge_begining, edge_ending, edge_weight in graph.edges:
            if dist[edge_begining] + edge_weight < dist[edge_ending]:
                dist[edge_ending] = dist[edge_begining] + edge_weight
                change = True
        if not change:
            return show_lenght(graph, dist)

    #checking for negative weight
    for edge_begining, edge_ending, edge_weight in graph.edges:
        if dist[edge_begining] + edge_weight < dist[edge_ending]:
            print("There is negative cycle in graph")
            return
    return show_lenght(graph, dist)

#printing in console
def show_lenght(graf, dystans):
    print("\n| Vertex | Lenght from starting_vertex:", graf.starting_vertex, "|")
    print("==========================================")
    for i in range(0, graf.number_of_vertexes):
        print("|   {:4s} |              {:17s} |".format(str(i), str(dystans[i]) if dystans[i] != float(np.inf) else "unreachable"))

#opening file
with open("graph.json", "r") as file:
    data = json.load(file)
g = Graph()
g.number_of_vertexes = len(data) - 1
for i in range(0, g.number_of_vertexes):
    for j in range(0, len(data[i])):
        g.edges.append([i, data[i][j][0], data[i][j][1]])

g.starting_vertex = data[-1]
BellmanFord(g)