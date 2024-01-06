import re
file = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/2022/day5/input.txt",'r').read()
c = file.split("\n")
instructions = file.split("\n\n")[1].split("\n")
print(instructions)

crate_lst = []
#Create crate lists
n = re.findall(r"\d+",c[3])
for numbers in n:
    crate_lst.append([])

#1. Populate crate lists
for i in range(3):
    crates = re.findall(r"[A-Z]|  [\s]",c[i])
    for j,crate in enumerate(crates):
        crate_lst[j].append(crate)
print(crate_lst)

instructions_list = []
#2. Decode instruction set
for move in instructions:
    instructions_list.append(re.findall("\d",move))
print(instructions_list)

#3. Apply instructions to crate lists