import re
#inputting in text file of strings
input1 = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_7/input.txt",'r').read().split('\n')

hands = []
hand_counts = []

#Probably a better way of doing this
ranks = {"A":14,
              "K":13,
              "Q":12,
              "J":11,
              "T":10,
              "9":9,
              "8":8,
              "7":7,
              "6":6,
              "5":5,
              "4":4,
              "3":3,
              "2":2
              }

#Create data structures 
for line in input1:
    sep = line.split(" ")
    count = []
    match = re.findall("(A|K|Q|J|T|9|8|7|6|5|4|3|2)", sep[0])
    card_types = set(match)
    for types in card_types:
        count.append(match.count(types))
    hands.append((match, int(sep[1])))
    hand_counts.append(count)

def classify_hand(hand_count:list):
    n = max(hand_count)
    if n ==5:
        return 6 #Five of a kind
    if n ==4:
        return 5 #Four of a kind
    if n == 3 and len(hand_count) ==2:
        return 4 #Full house
    if n ==3 and len(hand_count) ==3:
        return 3 #Three of a kind
    if n ==2 and len(hand_count) ==3:
        return 2 #Two pair
    if n ==2 and len(hand_count) ==4:
        return 1 #One pair
    if len(hand_count) ==5: 
        return 0 #High card
    return None

#TODO: Allow comparison between more than 2 cards
#If mutliple hands have the same rank, compares each card starting with the first to establish a stronger hand
def compare_hands(hands:list): 
    rank_list = []

    #Sort hands in order of rank for each element, starting with First
    for i in range(len(hands)):
        for j in range(5):
            rank_list.append(ranks[hands[i][0][j]]) 
    ordered_ranks = sorted(rank_list,reverse=True)
    print(ordered_ranks)
    return None

def rank_hands():
    sum_winnings = 0
    types = []
    totals = []
    for i,hand in enumerate(hand_counts):
        hand_type = (classify_hand(hand))
        types.append((hand_type,hands[i]))
        totals.append(hand_type)

    # #Hands primarily ordered based on type
    ordered_n = sorted(totals,reverse=True)
    ordered_types = sorted(types, reverse=True)
    n_strongest = ordered_n.count(ordered_n[0])
    if n_strongest ==1:
        mulitplier = 5
        for hand in ordered_types:
            sum_winnings +=hand[1][1] *mulitplier
    if n_strongest >1:
        hand_compare = []
        for i in range(n_strongest): hand_compare.append(ordered_types[i][1][0])
        strongest = compare_hands(hand_compare)
    return sum_winnings


    #If two hands have same type: Secondary ordering, 
    #first card in each hand is compared, stronger card wins