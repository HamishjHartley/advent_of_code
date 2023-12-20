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

#If two hands have the same rank, compares each card starting with the first to establish a stronger hand
def compare_hands(hands:list):
    h1, h2 = hands[0][0],hands[1][0]
    print("Comparing: ", h1, " + ", h2)
    for i in range(5):
    #First card
        if ranks[h1[i]] == ranks[h2[i]]:
            continue #Skip to next iteration
        if ranks[h1[i]] > ranks[h2[i]]:
            return h1
        else:
            return h2
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
    print(ordered_types)
    if n_strongest ==1:
        mulitplier = 5
        for hand in ordered_types:
            sum_winnings +=hand[1][1] *mulitplier

    return sum_winnings


win = compare_hands((hands[3],hands[2]))

print(win)



    #If two hands have same type: Secondary ordering, 
    #first card in each hand is compared, stronger card wins