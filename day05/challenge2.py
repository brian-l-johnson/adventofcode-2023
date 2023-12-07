#!/usr/bin/env python3

import sys
import math
import re
from datetime import datetime


def fill_map(map, dst, src, count):
    offset = dst-src;
    map.append((src, src+count ,offset))

def lookup_value(map, value):
    value = int(value)
    for range_def in map:
        if value >= range_def[0] and value <= range_def[1]:
            return value+range_def[2]
    return value

answer = math.inf
seeds = []
section = ""
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

seeds_re = re.compile("^seeds: (\d+ )+")
map_section_re = re.compile(r"^[a-z\-]+ map:$")
map_def_re = re.compile("^\d+ \d+ \d+$")

for line in sys.stdin:
    line = line.rstrip()
    if seeds_re.match(line):
        print("in seed section")
        seeds = line.split(": ")[1].split(" ")
    elif line == "":
        print("switching sections")
        section = ""
    elif map_section_re.match(line):
        print("found map definition header")
        section =  line.split(" ")[0]
    elif map_def_re.match(line):
        print(f"in map range definition for section {section}")
        range_def = line.split(" ")
        src = int(range_def[0])
        dst = int(range_def[1])
        count = int(range_def[2])
        match section:
            case "seed-to-soil":
                fill_map(seed_to_soil, src, dst, count)
            case "soil-to-fertilizer":
                fill_map(soil_to_fertilizer, src, dst, count)
            case "fertilizer-to-water":
                fill_map(fertilizer_to_water, src, dst, count)
            case "water-to-light":
                fill_map(water_to_light, src, dst, count)
            case "light-to-temperature":
                fill_map(light_to_temperature, src, dst, count)
            case "temperature-to-humidity":
                fill_map(temperature_to_humidity, src, dst, count)
            case "humidity-to-location":
                fill_map(humidity_to_location, src, dst, count)
            case _:
                print("unrecognized section")
                exit(-1)       
    else:
        print("unrecognized line!")    
        exit(-1)
print(seeds)
print(seed_to_soil)
print(soil_to_fertilizer)

print(len(seeds))

for i in range(int((len(seeds))/2)):
    print(f"on seed range {i}")
    for seed in range(int(seeds[2*i]), int(seeds[2*i])+int(seeds[2*i+1])):
        soil = -1
        fertilizer = -1
        water = -1
        light = -1
        temperature = 1
        humidity = -1
        location = -1

        soil = lookup_value(seed_to_soil, seed)
        fertilizer = lookup_value(soil_to_fertilizer, soil)
        water = lookup_value(fertilizer_to_water, fertilizer)
        light = lookup_value(water_to_light, water)
        temperature = lookup_value(light_to_temperature, light)
        humidity = lookup_value(temperature_to_humidity, temperature)
        location = lookup_value(humidity_to_location, humidity)

        #print(f"{seed}->{soil}->{fertilizer}->{water}->{light}->{temperature}->{humidity}->{location}")

        #print(f"seed {seed} should be in location {location}")

        location = int(location)

        if location < answer:
            answer = location
            print(f"{datetime.now()}:Seed:{seed}:location:{answer}")
print(answer)