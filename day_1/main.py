#inputting in text file of strings
with open('C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_1/input.txt') as f:
    lines = f.readlines()
    
num_list = []

for string in lines:
    line_value = []

    for i in range(len(string)):
        if string[i].isnumeric() == True:
            line_value.append(string[i])
    
    num_list.append(int(line_value[0]+line_value[-1]))

print(sum(num_list))
