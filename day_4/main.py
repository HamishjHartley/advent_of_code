import re
#inputting in text file of strings
input1 = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_4/input.txt",'r').read()
input1 =input1.split('\n')

#Win copies of scratch cards below the winning card equal to n_matches
#For each of these copies: win copies of scratch cards below the winning card equal to n_matches
#Until finished processing entire number of cards
#Cards will never make a copy of a card past the end of the table

card_totals = []

#Returns winning and actual numbers per card
def sep_cards(card_list:list):
    cards = []
    for i,line in enumerate(card_list):
        sep = line.split("|")
        w = re.findall(r"(\d+)", sep[0])
        del w[0] #To delete first entry in list(Not needed)
        a = re.findall(r"(\d+)",sep[1])
        cards.append((w,a))
    return cards

cards = sep_cards(input1)

#Returns total matches between winning and actual of a given card(If any)
def compare_match(winning:list, actual:list):
    total= 0
    for w_number in winning: 
        for a_number in actual:
            if w_number == a_number:
                total +=1 
    return total

def process_cards(cards:list):
    #1.Process cards to get total of matches per card

    #2. Create 1 copy for next n_matches cards 

    #3. 

    for i in range(len(cards)):
        print("Line number", i)
        total = 0
        total += compare_match(cards[i][0], cards[i][1])
        print("Next ",total, " Lines:")
        for j in range(total):
            card = re.findall(r"\d:", input1[i+j])
            card_num = int(card[0][0])
            card_totals.append(card_num)
            #compare_match(winning[card_num], actual[card_num])

        print(card_totals)
    return None

process_cards(cards)