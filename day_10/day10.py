file = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_10/input.txt",'r').read().split('\n')
#How many steps along the loop does it take to get from the starting position 
#to the point farthest from the starting position?

#(N,S,E,W) 

#1. Define pipe types
pipes = {(1,-1,0,0):"|",(0,0,-1,1):"-",(1,0,1,0):"L"}
#2. Identify continuous loop using the pipe types, starting with "S"
for i,line in enumerate(file):
    for j,char in enumerate(line):
        if char =="S":
            print(i,j)
#3. Count each step taken in pipe-grid

#4. Half this total

