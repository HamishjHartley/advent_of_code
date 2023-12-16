import re
#inputting in text file of strings
input1 = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_4/input.txt",'r').read()
input1 =input1.split('\n')

counter = []

def compare_numbers(winning,actual):
    total = 0
    for w_number in winning: 
        for a_number in actual:
            if w_number == a_number:
                total +=1
    return total

#Populates cards dictionary with n_matches per card
def populate_cards(input_list:list):
    cards = {}

    for i,line in enumerate(input1):
        sep = line.split("|")
        actual = re.findall(r"(\d+)",sep[1])
        winning = re.findall(r"(\d+)", sep[0])
        del winning[0] #To delete first entry in list(Not needed)

        total = compare_numbers(winning,actual)
        cards[i+1] =total 
    return cards

cards= populate_cards(input1)

def process_card(card_number:int):
    if card_number == len(cards):
        return
    else:
        for j in range(cards[card_number]):
            #print(cards[card_number+j+1]) 
            process_card(card_number+j+1)
            counter.append(1)

for i in range(len(cards)):
    process_card(i+1)

print(sum(counter)+207)

