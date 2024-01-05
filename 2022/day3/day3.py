file = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/2022/day3/input.txt",'r').read().split("\n")
priority_lst = []

for rucksack in file:
    first,second = rucksack[:len(rucksack)//2],rucksack[len(rucksack)//2:]
    unique = set(rucksack)
    for char in unique:
        if char in first and char in second:
            if char.isupper()==True:
                priority_lst.append(ord(char)-38)
            else:
                priority_lst.append(ord(char)-96)

print(sum(priority_lst))