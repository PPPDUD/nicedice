#!/usr/bin/python3
import random, json, sys

def roll_die(die):
    return str(random.randint(die["min"], die["max"]))

def pick_item(die):
    return random.choice(die["items"])

def weighted_item(die):
    return random.choices(die["items"], die["weights"], k=1)[0]

def handle_rng(die):
    if die["type"] == "die":
        return die["prefix"] + roll_die(die) + die["suffix"]
    elif die["type"] == "pick_items":
        return die["prefix"] + pick_item(die) + die["suffix"]
    elif die["type"] == "weighted_items":
        return die["prefix"] + weighted_item(die) + die["suffix"]

if len(sys.argv) == 1:
    print("Not enough arguments, exiting.", file=sys.stderr)
    sys.exit(64)
else:
    for i in sys.argv[1:]:
        f = open(i)
        die = json.loads(f.read())
        f.close()
        print(handle_rng(die))