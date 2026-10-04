# selected problem statement is: in memory database

import json


def SET(key, value):
    dict[key] = value
    print("key-value pair generated successsfuly :)")


def GET(key):
    try:
        print(dict[key])
    except KeyError:
        print("no such key found :( ")


def DEL(key):
    try:
        del dict[key]
    except KeyError:
        print("no such key exists :(")


def EXISTS(key):
    if key in dict:
        print("the key exists!")
    else:
        print("the key does not exist :(")


def SAVE():
    with open("file.txt", "w") as file:
        json.dump(dict, file)


def LOAD():
    with open("file.txt", "r") as file:
        global dict
        dict = json.load(file)


print("WELCOME user! \n this CLI interface takes in a supported function followed by required fields separated by a COMMA AND NO SPACE as input and gives the output accordingly ;) \n\n\n suported functions are : GET, SET, DEL, SAVE, EXISTS, LOAD")

dict = {}

while True:

    usr_input = input("enter the command : ")
    trunc_input = usr_input.strip()
    refined_input = trunc_input.split(",")

    if not refined_input:
        continue
    elif refined_input[0] == "SET" or refined_input[0] == "set":
        if len(refined_input)<3:
            print("not valid format try again")
        else:
            SET(refined_input[1], refined_input[2])
    elif refined_input[0] == "GET" or refined_input[0] == "get":
        if len(refined_input)<2:
            print("invalid format try again")
        else:
            GET(refined_input[1])
    elif refined_input[0] == "DEL" or refined_input[0] == "del":
        if len(refined_input)<2:
            print("invalid format try again")
        else:
            DEL(refined_input[1])
    elif refined_input[0] == "EXISTS" or refined_input[0] == "exists":
        if(refined_input)<2:
            print("invalid format try again")
        else:
            EXISTS(refined_input[1])
    elif refined_input[0] == "SAVE" or refined_input[0] == "save":
        SAVE()
    elif refined_input[0] == "LOAD" or refined_input[0] == "load":
        LOAD()
    elif refined_input[0] == "EXIT" or refined_input[0] == "exit":
        break
    else:
        print("not a valid command :(")
