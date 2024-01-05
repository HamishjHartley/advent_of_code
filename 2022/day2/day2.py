file = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/2022/day2/input.txt",'r').read().split("\n")
score = {"A X":3,"A Y":4,"A Z":8, "B X":1,"B Y":5,"B Z":9,"C X":2,"C Y":6,"C Z":7}
total =[]

#X LOSE
#Y DRAW 
#Z WIN

#A ROCK
#B PAPER
#C SCISSORS


for rounds in file:
    total.append((score[rounds]))

print(total)
print(sum(total))