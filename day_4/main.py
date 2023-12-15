import re
#inputting in text file of strings
input1 = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_4/input.txt",'r').read()
input1 =input1.split('\n')

line_points = []

#1. Separate Each line "|"
for i,line in enumerate(input1):
    total = 0 # Counter int
    print("line:", i)
    sep = line.split("|")
    winning = re.findall(r"(\d+)", sep[0])
    del winning[0] #To delete first entry in list(Not needed)
    actual = re.findall(r"(\d+)",sep[1])
    #2. Compare each element between winning numbers and actual numbers
    for w_number in winning: 
        for a_number in actual:
            if w_number == a_number:
                print("Winning number:", a_number)
                #3. Total matches if there are any
                total +=1
    if total ==1:
        line_points.append(1)
    if total>1:
        #point = 1, then double total-1 times
        point = 1
        for i in range(total-1):
            point = point*2
        line_points.append(point)

print(sum(line_points))

