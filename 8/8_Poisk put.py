# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 10:35:31 2024

@author: Admin
"""

import networkx as nx
import matplotlib.pyplot as plt

# Создание графа
G = nx.DiGraph()

# Добавление ребер
G.add_edge('a', 'b')
G.add_edge('b', 'c')
G.add_edge('b', 'd')

# Визуализация графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=10, font_color='black', arrowsize=20, arrowstyle='->')
plt.show()

# Функция для поиска пути в графе
def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
    return None

# Поиск пути от 'a' к 'c'
path_result = find_path(G.adj, 'a', 'c')

# Вывод результата
if path_result:
    print(f"Path from 'a' to 'c': {path_result}")
else:
    print("No path found.")
