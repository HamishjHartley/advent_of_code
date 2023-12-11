import re

input1 =["467..114.",
        "....*....",
        "....35..63",
        "3.,......#",
        "...,617*..",
        "....,.....",
        "+.58.,..59",
        "2.....,...",
        "...755.,..",
        ".$.*....,.",
        "664.598.."
]

input2= [
    "..*,.&....",
    ".*........",
    "..........",
    "...*......"
]

#Returns all adjecent positions, N, NE, NW, E, S, SE, SW, W for a symbol
def search_adjecent(symbol:tuple, input_list:list):
    search_pos = []
    line_num = symbol[0]
    index = symbol[1]

    #Dicitonary to store directions
    direction = {
        "N": (line_num-1,index),
        "NE":(line_num-1,index+1),
        "NW":(line_num-1,index-1),
        "W":(line_num,index-1),
        "S":(line_num+1,index),
        "SE":(line_num+1,index+1),
        "SW":(line_num+1,index-1),
        "E":(line_num,index+1)

    }
    for directions in direction:
        search_pos.append(direction[directions])
        x =[direction[directions]][0][1]
        y =[direction[directions]][0][0]
        print(input_list[x][y])
        #print(input_list[direction[directions]][0][1],input_list[direction[directions]][0][1])
    return search_pos

#iterate through input list
#return index of each symbol per line as a tuple (line number, line index)
def get_symbols(input_list:list):  
    symbols = []
    for i,line in enumerate(input_list):
        for j,char in enumerate(line):
            #checks if current character in line matches given set
            char_match = re.search(r"[*,$#&%+]+", char)

            #if character natches set record line index and number in symbols list
            if char_match != None:
                symbols.append((i,j))
    return symbols

symbols = get_symbols(input1)
search_adjecent(symbols[5],input1)


#if adjecent position contains number, regex that index on that line and capture full number
#Save each of these numbers in a list 
#Sum these numbers 

#print(symbols[0][1])
#print(numbers)