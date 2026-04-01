#!/usr/bin/python3
import json, sys, questionary
die = {}
die_type = questionary.select("What type of die are you hoping to create?", choices=["die", "pick_items", "weighted_items"]).ask()
die["type"] = die_type

if die_type == "die":
    die["min"] = int(input("What should the minimum number be? "))
    die["max"] = int(input("What should the maximum number be? "))
elif die_type == "pick_items":
    die["items"] = input("Please type a %-seperated list of possible items: ").split("%")
elif die_type == "weighted_items":
    die["items"] = input("Please type a %-seperated list of possible items: ").split("%")
    weights = input("Please type a %-seperated list of integer weights: ").split("%")
    new_weights = []
    for i in weights:
        new_weights.append(int(i))
    die["weights"] = new_weights

die["prefix"] = input("Prefix: ")
die["suffix"] = input("Suffix: ")

if len(sys.argv) >= 2:
    f = open(sys.argv[1], "w")
else:
    f = open(input("What should the filename be? "), "w")

f.write(json.dumps(die))
f.close()