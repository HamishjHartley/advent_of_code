#inputting in text file of strings
with open('C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/2024/day-1/input.txt') as f:
    lines = f.readlines()

left, right = [], []

for i in range(len(lines)):
    temp = lines[i].split("   ")
    left.append(int(temp[0]))
    right.append(int(temp[1]))

def distance():
    total = 0
    for i in range(len(left)):
        total += abs(min(left) - min(right))
        left.remove(min(left))
        right.remove(min(right))
    return total

def similarity():
    total = 0
    for i in range(len(left)):
        total += left[i] * right.count(left[i])
    return total

total = similarity()