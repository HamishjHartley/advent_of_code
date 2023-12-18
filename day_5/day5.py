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

maps = [seed_soil, soil_fert, fert_water, water_light, light_temp, temp_humid, humid_loc]

#3. Compute each seed through each map
def process_map(map:list, input_value:int):
    value = 0
    min_list = []
    max_list = []
    #for each line in map
    for i in range(len(map)): 
        srs = int(map[i][1])
        drs = int(map[i][0])
        r_length = int(map[i][2])
        min_list.append(srs)
        max_list.append(srs+r_length-1)
        if input_value >= srs and input_value < (srs+r_length):
            value = input_value + (drs-srs)
    #Checks if value is outwith mapped range
    if input_value <(min(min_list)) or input_value > (max(max_list)):
        value = input_value
    return value

loc_list = []
#For each seed find location and append to loc_list
for seed in seeds:
    value_list =[int(seed)]
    for i in range(len(maps)):
        value_list.append(process_map(maps[i],value_list[i]))
    loc_list.append(value_list[len(value_list)-1])

print(loc_list)

    
#print(value_list)

#print(process_map(humid_loc,78))
#4. Then for the following maps
#5. Find the lowest location number 