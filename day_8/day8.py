import re
from anytree import Node, RenderTree

#inputting in text file of strings
input1 = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_8/input.txt",'r').read().split('\n')

directions = input1[0]
node_list = []
dir_map= {"L":0,
          "R":1}

#https://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python
class Tree(object):
    "Generic tree node."
    def __init__(self, name='root', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)
    
#Populate tree dictionary
for i,line in enumerate(input1[2:len(input1)]):
    #Separating Parent node and children nodes from input text
    sep = line.split(sep=" = ")
    parent = sep[0]
    children = re.findall("[A-Z]+",sep[1])
    #1. Link parent node with previous parent node 
    curr_node = Tree(parent)
    #2. Add child nodes to parent node 
    for child in children: 
        curr_node.add_child(Tree(child))
    node_list.append((curr_node,curr_node.children))

#Traverse tree
for i,d in enumerate(directions):
    curr_search = node_list[0][1][dir_map[d]]
    print(curr_search)

    # for nodes in node_list:
    #     print(nodes)

#parent = nodes[0]
# L = nodes[1][0]
# R = nodes[1][1]