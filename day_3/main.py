import re
input ="467..114.....*........35..633.,......#...,617*......,.....+.58.,..592.....,......755.,...$.*....,.664.598.."

direction = {
    #N
    "n":-11,
    #NE
    "ne":-12,
    #NW
    "nw":-10,
    #E
    "e":1,
    #S
    "s":11,
    #SE
    "se":12,
    #SW
    "sw":0,
    #W
    "w":1
}

symbols, numbers = [],[]
for i,char in enumerate(input):
    #captures any character which is not a number or a dot
    symbols.append(re.findall(r"[^\d.]", char))
    numbers.append(re.findall(r"(\d)",char))

print(symbols)
print(numbers)
#print(flat_list) 
#flat_list (next row)
#print(flat_list[direction["w"]])