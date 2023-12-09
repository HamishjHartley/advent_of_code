import sys

line1 = "labc2"
line2 = "pqr3stu8vwx"
line3 = "a1b2c3d4e5f"
line4 = "treb7uchet"

with open('input.txt') as f:
    lines = f.readlines()

num_list = []

for i in range(len(line3)):
    if line3[i].isnumeric() == True:
        num_list.append(int(line3[i]))

print(num_list)