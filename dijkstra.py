import networkx as nx

from graph import metro_network

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    predecessors = {node: None for node in graph.nodes}
    unvisited = list(graph.nodes)
    visited = []

    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])

        if distances[current_node] == float('infinity'):
            break

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = distances[current_node] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node

        visited.append(current_node)
        unvisited.remove(current_node)

    # Reconstruct the path
    end_station = max(distances, key=distances.get)
    path = []
    current = end_station
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]

    # Calculate the total cost
    total_cost = distances[end_station]

    return path, total_cost

# Assuming you have a NetworkX graph named metro_network
start_station = "Холодна гора"
shortest_path, cost = dijkstra(metro_network, start_station)

print(f"Найкоротший шлях від {start_station}: {shortest_path}, Дальність: {cost} км")