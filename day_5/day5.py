import re
#inputting in text file of strings
input1 = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_5/input.txt",'r').read().split('\n')

#1. Create a seed_list, converts from string to int
seeds = list(map(int,re.findall(r"\d+", input1[0]))) 

new_seeds = []
for i in range(0,len(seeds),2):
    start = seeds[i]
    length = seeds[i+1]
    for j in range(length):
        new_seeds.append(start+j)
        print(start+j)


#2. Create lists to store the maps
def populate_map(target:str, list_name:str):
    list_name = []
    for i,lines in enumerate(input1):
        match = re.search(target, lines)
        if match != None:
            for j,lines in enumerate(input1):
                if i+j+1 >= len(input1):
                    return list_name
                elif input1[i+j+1] == '':
                    break
                else:
                    values = re.findall("\d+",input1[i+j+1])
                    list_name.append(values)
    return list_name

seed_soil = populate_map("(?=(seed-to-soil))", "seed_soil")
soil_fert = populate_map("(?=(soil-to-fertilizer))", "soil_fert")
fert_water =populate_map("(?=(fertilizer-to-water))", "fert_water")
water_light =populate_map("(?=(water-to-light))", "water_light")
light_temp =populate_map("(?=(light-to-temperature))", "light_temp")
temp_humid =populate_map("(?=(temperature-to-humidity))", "temp_humid")
humid_loc =populate_map("(?=(humidity-to-location))", "humid_loc")

#3. Compute each seed through each map
maps = [seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc]

#3. Computes a given seed through each map
def process_seed(seed:int):
    outwidth_flag = False
    for s_map in maps:
        for i in range(len(s_map)): #for each line in map
            drs = int(s_map[i][0])
            srs = int(s_map[i][1])
            r_length = int(s_map[i][2])
            if seed >= srs and seed < srs+r_length: #Check if seed value outwith these range
                seed = seed + (drs-srs)
                outwidth_flag = False
                break
            else: outwidth_flag = True
        if outwidth_flag ==True: outwidth_flag = False #No change
    return seed 

#4. For each seed: process seed and append value to list
# seed_values = []
# for seed in new_seeds:
#     seed_values.append(process_seed(seed))
# #5. Find minimum from seed result list
# print(min(seed_values))