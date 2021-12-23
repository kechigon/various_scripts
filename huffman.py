from heapq import heappush, heappop
from collections import deque

class Node:
    def __init__(self, value=None, frequency=None, zero=None, one=None):
        self.value = value
        self.frequency = frequency
        self.zero = zero
        self.one = one

    def __lt__(self, other):
        return self.frequency < other.frequency

def create_nodes(s):
    nodes = []
    chars = set(s)
    l = len(s)
    for char in chars:
        heappush(nodes, Node(char, s.count(char) / l))
    return nodes

def create_huffman_tree(nodes):
    while len(nodes) >= 2:
        low_frequency_1 = heappop(nodes)
        low_frequency_2 = heappop(nodes)
        heappush(nodes, Node(None, low_frequency_1.frequency + low_frequency_2.frequency, low_frequency_1, low_frequency_2))
    return heappop(nodes)

encode = {}
code = deque()
def encoding(node):
    global code
    if node.value != None:
        global encode
        encode[node.value] = list(code)
    if node.zero != None:
        code.append(0)
        encoding(node.zero)
    if node.one != None:
        code.append(1)
        encoding(node.one)
    if len(code) >= 1:
        code.pop()

s = input("input strings you want encode:")
nodes = create_nodes(s)
frequency = {}
for node in nodes:
    frequency[node.value] = node.frequency

print("frequency of each char")
print(frequency)
print()

huffman_tree = create_huffman_tree(nodes)
encoding(huffman_tree)

print("encode of each char")
print(encode)
print()