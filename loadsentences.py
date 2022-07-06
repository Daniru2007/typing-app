import random
import json

data = json.load(open("randomsentences.json"))["data"]

def rand_sentence():
    return data[random.randint(0,724)]["sentence"]
