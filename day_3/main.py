import re

input1 =["467..114..",
        "....*.....",
        "....35..63",
        "3.,......#",
        "...,617*..",
        "....,.....",
        "+.58.,..59",
        "2.....,...",
        "...755.,..",
        ".$.*....,.",
        "664.598..."
]

#Searches all adjecent positions, N, NE, NW, E, S, SE, SW, W for a given index and line in input_list
#Returns is_valid boolean
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
        print("Directions",directions[0],directions[1])
        x = directions[0]
        y = directions[1]
        #bounds of input list
        if x and y >= 0 and x <line_length and y <line_length:
            print(input_list[y][x], "at", x,"," ,y)
            char_match = re.search(r"[*,$#&%+]+", input_list[y][x])
            #if adjecent character is a symbol set is_valid flag to True and break
            if char_match != None:
                is_valid = True
                break
    return is_valid

#1.Search input string for numbers, save match object for each in number_list[]
def get_numbers(input_list:list):
    number_list = []
    valid_numbers = []

    for i,line in enumerate(input_list):
        number = re.findall(r"\d+", line)

        for numbers in number: 
            print("Number: ", numbers)
            match =re.search(numbers, line)
            start = match.span()[0]
            end = match.span()[1]
            #2. For each number in number_list[]: for each character in number search adjecent, 
            # if search adjecent == Symbol, set number_valid = True break, then append to valid_numbers[]; 
            for j in range(end - start):
                #print("searching adjecent to:", match.group()[i], ", position:", start, i) 
                #print(line[start+j])
                is_valid = search_adjecent((start+j), i, input_list) 
                if is_valid == True:
                    valid_numbers.append(numbers)
                    print(numbers, "Is valid")
                    break

    return valid_numbers

valid_numbers = get_numbers(input1)
print(valid_numbers)

#3. sum(valid_numbers[])