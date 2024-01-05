file = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/2022/day4/input.txt",'r').read().split("\n")
total = 0
for pair in file:
    elves = pair.split(",")
    l1, r1 = list(map(int,elves[0].split("-")))
    l2, r2, = list(map(int,elves[1].split("-")))
    #left 1 > left 2 and right1 < right2
    if l1 >= l2 and r1 <= r2:
        total+= 1
        print(elves,l1 ,">=", l2, "and", r1, "<=", r2)
        continue
    #or left2 > left1 and right2 < right1
    if l2 >= l1 and r2 <= r1:
        total+=1
        print(elves,l2 ,">=", l1, "and", r2, "<=", r1)
        continue

    
print(total)