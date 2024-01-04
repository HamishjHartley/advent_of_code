import re
from collections import Counter

#inputting in text file of strings
input1 = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_7/input.txt",'r').read().split('\n')

ranks = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14}
hands = []

five_kind = []
four_kind = []
full_house = []
three_kind = []
two_pair = []
one_pair = []
high_card = []

for line in input1: hands.append(line.split(" "))

#Inital sorting 
def sort_hands(hands:list):
    for hand in hands:
        res =Counter(hand[0])
        l = len(res)
        common = res.most_common()[0][0]
        m = res[common]
        print(hand, l, m)
        if l ==5:
            high_card.append(hand)
        if l==4:
            one_pair.append(hand)
        if l==3 and m==2:
            two_pair.append(hand)
        if l==3 and m==3:
            three_kind.append(hand)
        if l==2 and m==3:
            full_house.append(hand)
        if l==2 and m==4:
            four_kind.append(hand)
        if l==1:
            five_kind.append(hand)

#Sort hands Based on strength of each card left to right
def sort_type(hand_type:list):
    alphabet = "AKQT98765432J"
    s = sorted(hand_type, key=lambda hand: [alphabet.index(c) for c in hand[0]])
    return s

sort_hands(hands)

rank_list = [sort_type(five_kind), sort_type(four_kind), sort_type(full_house), sort_type(three_kind), sort_type(two_pair), sort_type(one_pair), sort_type(high_card)]

#Flatten list: https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
flat_list = [
    x
    for xs in rank_list
    for x in xs
]

winnings = 0
for i in range(len(flat_list)):
    rank = len(flat_list) -i
    winnings+=int(flat_list[i][1]) * rank

print(winnings)