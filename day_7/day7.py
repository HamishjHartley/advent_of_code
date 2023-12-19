import re
#inputting in text file of strings
input1 = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_7/input.txt",'r').read().split('\n')

hand_val = []
hand = []
hand_count = []
hand_types = []

ranks = [] #ranks of type of hand

#Put hands in order of strength
for i,line in enumerate(input1):
    temp = []
    hand_val.append(line.split(" "))
    hand.append(re.findall("(A|K|Q|J|T|9|8|7|6|5|4|3|2)", hand_val[i][0]))
    hand_types.append(set(hand[i])) #converting to a set so only unique values
    for card in hand_types[i]: 
        temp.append((hand[i].count(card), card))
    hand_count.append(temp)

def rank_hand(hand_count:list):
    n = max(hand_count)[0]
    #5 kind 
    if n==5:
        return 6
        print("5 of a kind") 
    # #4 kind
    if n==4:
        return 5
        print("4 of a kind") 
    # #Full house
    if len(hand_count) ==2 and n ==3:
        return 4
        print("Full house")
    #3 kind
    if n == 3:
        return 3
        print("3 of a kind")
    #2 pair
    if len(hand_count) ==3 and n==2:
        return 2
        print("2 pair")
    #1 pair
    if len(hand_count) ==4:
        return 1
        print("1 pair")
    #High card
    if len(hand_count) ==5:
        return 0
        print("High card")

#print(hand_count)

for hands in hand_count:
    ranks.append(rank_hand(hands))

print(ranks)
#4. Order hands in strength






#Determine total winnings, sum each hands bid with rank