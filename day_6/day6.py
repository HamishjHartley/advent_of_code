import re
#inputting in text file of strings
input1 = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_6/input.txt",'r').read().split('\n')

t= re.findall("\d+", input1[0])
d = re.findall("\d+",input1[1])

t = list(map(int, t))
d = list(map(int, d))

total_list = []

for i in range(len(t)):
    #print("\n")
    #print("Race ", i)
    button_press =0
    moving_time = 0
    total = 0
    for j in range(t[i]+1):
        moving_time = t[i] - button_press
        distance = button_press*moving_time
        if distance > d[i]:
            total+=1
        #print("Press button for: ",button_press, "time left:", moving_time, "Distance travelled: ", distance)
        button_press +=1
    total_list.append(total)

result = 1
for each in total_list:
    result = result * each

print(result)