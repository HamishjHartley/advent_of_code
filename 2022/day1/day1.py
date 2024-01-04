file = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/2022/day1/input.txt",'r').read().split("\n\n")
calories = []
for elf in file: calories.append(sum(list(map(int,elf.split("\n")))))
print(sum(sorted(calories,reverse=True)[0:3]))