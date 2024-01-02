import re
#inputting in text file of strings
input1 = open("C:/Users/theha/OneDrive/Documents/GitHub/advent_of_code/day_5/input.txt",'r').read().split('\n')

#1. Create a seed_list
seeds = re.findall(r"\d+", input1[0])

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
        #for each line in map
        for i in range(len(s_map)): 
            print(i)
            drs = int(s_map[i][0])
            srs = int(s_map[i][1])
            r_length = int(s_map[i][2])
        #Check if seed value outwith these range
            if seed >= srs and seed < srs+r_length:
                seed = seed + (drs-srs)
                print("Changed by", drs-srs)
                outwidth_flag = False
                break
            else:
                outwidth_flag = True
        if outwidth_flag ==True:
            print("Not in range")
            seed = seed #No change
            outwidth_flag = False
        print(seed)
    return seed 

process_seed(79)


# loc_list = []
# #For each seed find location and append to loc_list
# for seed in seeds:
#     #print("\n")
#     #print("Seed number:", seed)
#     value_list =[int(seed)]
#     for i in range(len(maps)):
#         #print("Processing:",value_list[i], " with:", i) 
#         value_list.append(process_map(maps[i],value_list[i]))
#     loc_list.append(value_list[-1])
#     #print("Processed:", seed, "final value:", value_list[len(value_list)-1])

#print(min(loc_list))
#print(loc_list)

#4. Then for the following maps
#5. Find the lowest location number 
#1,3,7,17