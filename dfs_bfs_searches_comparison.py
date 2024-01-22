import networkx as nx
import matplotlib.pyplot as plt

from queue import deque

from graph import metro_network, pos


def dfs_paths(graph, vertex, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(vertex)
    path.append(vertex)

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_paths(graph, neighbor, visited, path)

    return path


def bfs_paths(graph, queue, visited=None):
    if visited is None:
        visited = set()

    path = []

    if not queue:
        return path

    vertex = queue.popleft()

    if vertex not in visited:
        path.append(vertex)
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)

    path += bfs_paths(graph, queue, visited)
    return path


# Візуалізація графу
nx.draw(metro_network, pos=pos, with_labels=True, font_weight='bold',
        node_color='lightblue', edge_color='gray', node_size=800,
        font_size=8, font_color='black')

# Додавання назви графу як заголовку
plt.title(metro_network.name)

plt.show()

# Використання DFS і BFS для знаходження шляхів
start_station = "Холодна гора"

path_dfs = dfs_paths(metro_network, start_station)
print("DFS шлях:", path_dfs)
print(f"{'-'*183}")
path_bfs = bfs_paths(metro_network, deque([start_station]))
print("BFS шлях:", path_bfs)