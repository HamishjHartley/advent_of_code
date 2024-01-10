file = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/2022/day6/input.txt",'r').read().split("\n")

for data in file:
    for i in range(len(data)-4):
        print(data[i],data[i+1],data[i+2],data[i+3])
        sample = data[i]+data[i+1]+data[i+2]+data[i+3]
        if len(set(sample))== len(sample):
            print(i+4,"Characters processed")
            break
