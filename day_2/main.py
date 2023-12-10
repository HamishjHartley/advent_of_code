import re
import numpy as np

#inputting in text file of strings
with open('C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_2/input.txt') as f:
    lines = f.readlines()
    
input = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

#The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

#regex input list to separate sets, then terms per colour

#total terms per set
#check against 12 red, 13 green, 14 blue rule, return True if agrees with rule
#keep record of game number id
#total possible game number id list

set_list = []
game_list = []

for i,line in enumerate(input):
    line = line.split(sep=";")
    #print(line)
    for group in line:
        match = re.findall(r"(?=(\d blue|\d red|\d green))",group)
        set_list.append(match)
        #print(line[0])
        #print(match)
        #print(group)
    
    match = re.findall(r"(\d:)",input[i]) 
    game_list.append(match)

    #print(match)
    #print(set_list[i])

print(set_list)
#print(game_list)