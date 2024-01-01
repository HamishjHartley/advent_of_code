import re
#inputting in text file of strings
input1 = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_9/input.txt",'r').read().split('\n')

counter = 0 #To sum extrapolated last values

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
def process_seq(seq:list, history:list):
    if is_zero(seq) ==True:
        return history
    else:
        diff = get_diff(seq)
        history.append(diff)
        return process_seq(diff,history)
    
def extrapolate(history:list):
    #Does the lists in wrong order(Top down)
    for i in reversed(range(len(history))):
        curr = i
        if is_zero(history[curr]) == True:
            history[curr].append(0) # Add 0 to first seq in history
            continue 

        left = history[curr][-1] #last value in list

        below = history[curr+1][-1] #Last value of below list  
        history[curr].append(left+below)
    print("Extrapolated: ", history)
    return history

def extrapolate_back(history:list):
    #similar to extrapolate but append to start of list rather than end, 

    #1. Minus the first value of the below list from the the first value on current list

    #2. Insert this value to start of list
    for i in reversed(range(len(history))):
        curr = i
        if is_zero(history[curr]) == True:
            history[curr].insert(0,0) # Add 0 to first seq in history
            continue 

        right = history[curr][0] #First value in list
        below = history[curr+1][0] #First value of below list  S
        history[curr].insert(0,(right-below))
    print("Extrapolated back", history)
    return history

for i,line in enumerate(input1):
    print("Line:",i)
    numbers = list(map(int,re.findall("[-]?\d+", line))) #Gets list of numbers, casts from str to int

    history = process_seq(numbers,[])
    history.insert(0,numbers)
    ex = extrapolate_back(history)

    counter += ex[0][0]

print(counter)