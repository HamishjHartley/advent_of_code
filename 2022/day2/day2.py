file = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/2022/day2/input.txt",'r').read().split("\n")
score = {"A X":4,"A Y":8,"A Z":3, "B X":1,"B Y":5,"B Z":9,"C X":7,"C Y":2,"C Z":6}
total =[]
for rounds in file:
    total.append((score[rounds]))
print(sum(total))