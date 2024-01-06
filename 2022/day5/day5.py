import re
file = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/2022/day5/input.txt",'r').read().split("\n")

crate_lst = []
#Create crate lists
n = re.findall(r"\d+",file[3])
for numbers in n:
    crate_lst.append([])

#1. Populate crate lists
for i in range(3):
    crates = re.findall(r"[A-Z]|  [\s]",file[i])
    print(crates)
    for j,crate in enumerate(crates):
        crate_lst[j].append(crate)
print(crate_lst)
    #Combine two spaces into one
#2. Decode instruction set

#3. Apply instructions to crate listsjhj7