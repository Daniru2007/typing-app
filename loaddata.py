import random
import json

with open("randomsentences.json") as file:
    sentences = json.load(file)["data"]

with open("data.json") as file:
    data = json.load(file)


def rand_sentence():
    return sentences[random.randint(0,724)]["sentence"]


def get_best():
    return data["best"]


def get_username():
    return data["username"]


def set_username(username):
    data["username"] = username
    with open("data.json", "w") as file:
        json.dump(data, file)


def set_best(new_best):
    data["best"] = new_best
    with open("data.json", "w") as file:
        json.dump(data, file)
