import re
from anytree import Node, RenderTree

#inputting in text file of strings
input1 = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_8/input.txt",'r').read().split('\n')

directions = input1[0]
tree= {}
dir_map= {"L":0,
          "R":1}

#Populate tree dictionary
for i,line in enumerate(input1[2:len(input1)]):
    sep = line.split(sep=" = ")
    parent = sep[0]

    children = re.findall("[A-Z]+",sep[1])

    tree[parent] = children

def search_tree(tree:dict):
    for i,nodes in enumerate(tree):
        for direction in directions:
            curr = tree[nodes][dir_map[direction]]
            print(curr,i)
            if curr == "ZZZ":
                print(i, "Steps required")
                return i
            
print(directions)
n_steps = search_tree(tree)