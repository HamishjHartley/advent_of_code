import re
file = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/2022/day5/input.txt",'r').read()
c = file.split("\n")
instructions = file.split("\n\n")[1].split("\n")

crate_lst = []
#Create crate lists
n = re.findall(r"\d+",c[8])
for numbers in n:
    crate_lst.append([])

#1. Populate crate lists,and reverse them
for i in range(len(crate_lst)):
    crates = re.findall(r"[A-Z]|   [\s]",c[i])
    for j,crate in enumerate(crates):
        if crate != "   " and crate != "    ":
            crate_lst[j].append(crate)

for i in range(len(crate_lst)):
    crate_lst[i].reverse()
print(crate_lst)

#2. Decode instruction set
#3. Apply instructions to crate lists
for i,move in enumerate(instructions):
    print(instructions[i])
    m = re.findall("\d+",move)
    m = list(map(int,m)) 
    amount = m[0]
    origin = m[1]-1
    destination = m[2]-1
    print(amount,origin,destination)
    for i in range(amount):
        crate_lst[destination].append(crate_lst[origin].pop())
        print(crate_lst[origin],">>",crate_lst[destination])
#         #print(crate_lst[origin],crate_lst[destination])
    print(crate_lst)
