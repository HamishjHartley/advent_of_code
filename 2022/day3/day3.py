file = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/2022/day3/input.txt",'r').read().split("\n")
priority_lst = []

#Split file line input every 3 lines
for i in range(0, len(file),3):
    first = file[i]
    second= file[i+1]
    third = file[i+2]
    group = first + second+third
    unique = set(group)
    for char in unique:
        if char in first and char in second and char in third:
            if char.isupper()==True:
                priority_lst.append(ord(char)-38)
            else:
                priority_lst.append(ord(char)-96)

print(sum(priority_lst))
