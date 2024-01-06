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


#2. Decode instruction set
#3. Apply instructions to crate lists
for move in instructions:
    m = re.findall("\d",move)
    m = list(map(int,m)) 
    m = [x-1 for x in m]
    print(m)
    amount = m[0]
    origin = m[1]
    destination = m[2]
    for i in range(amount):
        crate_lst[destination].append(crate_lst[origin].pop())

print(crate_lst)