import re
#inputting in text file of strings
input1 = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_9/input.txt",'r').read().split('\n')

#Extrapolate the history for each line of data

#Get difference between each number and append this to a new list
def get_diff(input:list):
    diff_list = []
    for i in range(len(input)-1):
        difference = input[i+1] - input[i] 
        diff_list.append(difference)
    return diff_list

#Checks if all elements of list are 0
def is_zero(input:list):
    if all(v == 0 for v in input):
        return True
    else:
        return False
    
#Recursive function which processes each sequence of a line until is_zero ==True
def process_seq(seq:list):
    if is_zero(seq) ==True:
        #Extrapolate
        
        return seq
    else:
        diff = get_diff(seq)
        print(diff)
        process_seq(diff)
    

for i,line in enumerate(input1):
    print("Line:",i)
    numbers = list(map(int,re.findall("\d+", line))) #Gets list of numbers, casts from str to int

    process_seq(numbers)

