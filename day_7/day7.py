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
        m = res[max(res)]
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
    alphabet = "AKQJT98765432"
    
    s = sorted(hand_type, key=lambda hand: [alphabet.index(c) for c in hand[0]])
    print(s)
    return s


sort_hands(hands)
sort_type(four_kind)

rank_list = [sorted(five_kind,reverse=True), sorted(four_kind,reverse=True), sorted(full_house), sorted(three_kind), sorted(two_pair), sorted(one_pair), sorted(high_card)]

#Flatten list: https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
flat_list = [
    x
    for xs in rank_list
    for x in xs
]



