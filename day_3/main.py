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

#iterate through input list
#return index of each symbol per line as a tuple (line number, line index)
symbols, numbers = [],[]
for i,line in enumerate(input1):
    #print(line)
    for j,char in enumerate(line):
        #checks if current character in line matches given set
        char_match = re.search(r"[*,$#&%+]+", char)
        num_match = re.search(r"[(\d+)]", char)
        #if character natches set record line index and number in symbols list
        if char_match != None:
            symbols.append((i,j))
        if num_match != None:
            numbers.append((i,j))

#search all adjecent positions, N, NE, NW, E, S, SE, SW, W for each symbol
def search_adjecent(symbol:tuple):
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
        print(direction[directions])
#if adjecent position contains number, regex that index on that line and capture full number
#Save each of these numbers in a list 
#Sum these numbers 

search_adjecent(symbols[0])
#print(symbols[0][1])
#print(numbers)



