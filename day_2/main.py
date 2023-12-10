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
possible_game = []

colour_limit = {"red":12,
                "green":13,
                "blue":14
}

#For each game
for i,line in enumerate(lines):
    line = line.split(sep=";")
    #print(line)

    #regex for game number
    game_number = re.findall(r"(\d\d:|\d:)",lines[i])
    #splitting game number string to int value
    game_number = game_number[0].split(sep=":")[0]
     

    possible_sets = 0 

    #print("game number:",game_number)
    #for each set in each game
    for i,group in enumerate(line):
        poss_values = 0 #totals possible elements 
        n_sets = i #totals number of sets per game
        

        #print("set number",i)
        match = re.findall(r"(?=(\d blue|\d red|\d green|\d\d blue|\d\d red|\d\d green))",group)
        set_list.append(match)

        #for each element in set
        for i in range(len(match)):
            compare = match[i].split(sep=" ")

            #compare each element of set with possible limit for each colour
            if int(compare[0]) < colour_limit[compare[1]]:
                #print(compare, "Possible")
                poss_values+=1 

        #if the amount of possible values equals total values in set, set is possible
        if poss_values == len(match):
            possible_sets= possible_sets+1
            #print("added set")
    #print(possible_sets)
    #print(n_sets+1)

    if possible_sets == n_sets+1:
        possible_game.append(int(game_number))
        #print("Possible game", game_number)
            
print(possible_game)
print(sum(possible_game))