import re

#inputting in text file of strings
with open('C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_1/input.txt') as f:
    lines = f.readlines()
    
num_list = []

num_dict = {"one":1,
            "two" :2,
            "three":3,
            "four":4,
            "five":5,
            "six":6,
            "seven":7,
            "eight":8,
            "nine":9,
}    

for line in lines:
    match = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)

    print(match)
    #check each line if it contains any of num dict entries
    for i,element in enumerate(match):
        if element.isnumeric() == False:
            match[i] = str(num_dict[element]) 

    print(match)
    num_list.append(int(match[0]+match[-1]))

print(sum(num_list))