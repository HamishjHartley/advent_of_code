import re

#inputting in text file of strings
with open('C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_2/input.txt') as f:
    lines = f.readlines()

totals_sqrd = []
for i,line in enumerate(lines):
    totals = {'r':0,'b':0,'g':0}
    game_sets = line.split(sep=";")
    for s in game_sets:
        set_values = re.findall(r"(\d+)\s(\w)",s)
        for each in set_values :
            if totals[each[1]] < int(each[0]):
                totals[each[1]] = int(each[0])
    totals_sqrd.append(totals["b"] * totals["r"] * totals["g"])

print(sum(totals_sqrd))