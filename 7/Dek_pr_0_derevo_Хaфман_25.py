# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 00:22:16 2023

@author: Admin
"""

import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    frequency = Counter(data)
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left, merged.right = left, right
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(node, code="", mapping=None):
    if mapping is None:
        mapping = {}

    if node.char:
        mapping[node.char] = code
    if node.left:
        build_huffman_codes(node.left, code + "0", mapping)
    if node.right:
        build_huffman_codes(node.right, code + "1", mapping)

    return mapping

def huffman_encode(data, mapping):
    encoded_data = "".join(mapping[char] for char in data)
    return encoded_data

def huffman_decode(encoded_data, root):
    decoded_data = ""
    current_node = root

    for bit in encoded_data:
        if bit == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decoded_data += current_node.char
            current_node = root

    return decoded_data

if __name__ == "__main__":
    message = "huffman coding example"
    
    # Строим дерево Хаффмана
    huffman_tree = build_huffman_tree(message)
    
    # Строим таблицу кодирования
    huffman_mapping = build_huffman_codes(huffman_tree)
    
    # Кодируем сообщение
    encoded_message = huffman_encode(message, huffman_mapping)
    
    # Декодируем сообщение
    decoded_message = huffman_decode(encoded_message, huffman_tree)
    
    print("Original Message:", message)
    print("Encoded Message:", encoded_message)
    print("Decoded Message:", decoded_message)
