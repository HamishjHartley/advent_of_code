import re
#inputting in text file of strings
input1 = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_3/input.txt",'r').read().split('\n')

#Searches all adjecent positions, N, NE, NW, E, S, SE, SW, W for a given index and line in input_list, Returns is_valid boolean
def search_adjecent(index:int, line_num:int, input_list:list):
    is_valid = False #Boolean flag 
    line_length = len(input_list[0]) 
    #Dicitonary to store directions
    direction = [
        (line_num-1,index), #North
        (line_num-1,index+1), #North East
        (line_num-1,index-1), #North West
        (line_num,index+1), #East
        (line_num,index-1), #West
        (line_num+1,index), #South
        (line_num+1,index+1), #South East
        (line_num+1,index-1) #South West
    ]
    for directions in direction:
        x = directions[0]
        y = directions[1]
        if x >= 0 and y >= 0 and x <line_length and y <line_length: #bounds of input list
            char_match = re.search(r"[*,$#&%+=@]", input_list[x][y])
            if char_match != None:  #if adjecent character is a symbol set is_valid flag to True and break
                is_valid = True
                break
    return is_valid

#1.Search input string for numbers, for each number check if adjecent to symbol, if number is valid: append to valid_numbers[], Returns valid_numbers list
def get_numbers(input_list:list):
    valid_numbers = []
    for i,line in enumerate(input_list):
        number = re.findall(r"\d+", line)
        for numbers in number: 
            match =re.search(numbers, line)
            start = match.span()[0]
            end = match.span()[1]
            #2. For each number per line: for each character in number search adjecent, 
            for j in range(end - start):    # if search adjecent == Symbol, set number_valid = True break, then append to valid_numbers[]; 
                is_valid = search_adjecent((start+j), i, input_list) 
                if is_valid == True:
                    valid_numbers.append(int(numbers))
                    print("valid number:", numbers)
                    break
    return valid_numbers

valid_numbers = get_numbers(input1)
print(sum(valid_numbers)) #3. sum(valid_numbers[])