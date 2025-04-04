# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 00:38:36 2024

@author: Admin
"""

from itertools import product

def coloring(graph, colors):
    vertices = get_vertices(graph)
    assign_colors(vertices, colors)
    return valid_coloring(graph)

def get_vertices(graph):
    return set(vertex for edge in graph for vertex in edge[0])

def assign_colors(vertices, colors):
    for vertex, color in zip(vertices, colors):
        assign_color(vertex, color)

def assign_color(vertex, color):
    color_assignment[vertex] = color

def valid_coloring(graph):
    for edge in graph:
        vertex, neighbors = edge[0], edge[1]
        vertex_color = color_assignment[vertex]
        neighbor_colors = {color_assignment[neighbor] for neighbor in neighbors}
        if vertex_color in neighbor_colors:
            return False
    return True

# Пример использования
graph = [('a', ['b', 'c', 'd']),
         ('b', ['a', 'c']),
         ('c', ['a', 'b', 'd']),
         ('d', ['a', 'c'])]

color_assignment = {}

# Пример запроса
result = coloring(graph, ['red', 'green', 'blue', 'yellow'])
print(result)
