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
#return index of each symbol per line

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


#print(symbols)
#print(numbers)

for i in symbols:
    print(input1[i])

