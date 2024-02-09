import os
from password_generator import *


if not os.path.exists("master_password.txt"):
    master = input("create your master password: ")
    with open("master_password.txt", "w") as f:
        f.write(master)

with open("master_password.txt" , "r") as masterfile:
    masterPwd = masterfile.read()

correctMaster = False

while not correctMaster:
    inputMaster = input("enter the master password: ")
    if inputMaster == masterPwd:
        correctMaster = True
    else:
        print("incorrect password, try again")

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            print(line.rstrip())

def add():
    name = input("account name: ")
    pwd = input("password: ")

    with open("password.txt", "a") as f:
        f.write("account name: " + name + " , password: " + pwd + "\n")

def generate(typen):
    if typen == "1":
        print(type1)
        use = input("do you want to use the password: ")
        if use == "y":
            name = input("name: ")
            with open("password.txt", "a") as f:
                f.write("name: " + name + " , pwd: " + type1 + "\n")
    elif typen == "2":
        print(type2)
        use = input("do you want to use the pwd: ")
        if use == "y":
            name = input("name: ")
            with open("password.txt", "a") as f:
                f.write("name: " + name + " , pwd: " + type2 + "\n")
    elif typen == "3":
        print(type3)
        use = input("do you want to use the pwd: ")
        if use == "y":
            name = input("name: ")
            with open("password.txt", "a") as f:
                f.write("name: " + name + " , pwd: " + type3 + "\n")
    elif typen == "4":
        print(type4)
        use = input("do you want to use the pwd: ")
        if use == "y":
            name = input("name: ")
            with open("password.txt", "a") as f:
                f.write("name: " + name + " , pwd: " + type4 + "\n")

def changeMaster():
    newMaster = input("create your new master password: ")
    with open("master_password.txt", "w") as f:
        f.write(newMaster)


def help():
    print("0 will represent a two digit number, for example: 12")
    print("word will represent a word from english, for example: Listen")
    print("? will represent a special character, for example: ( or =")
    print("type 1 password: 0word0word0")
    print("type 2 password: 0word0word??")
    print("type 3 password: 00word?word??")
    print("type 4 password: its an all random password using a combination of any ascii symbols")


while True:
    mode = input("Select mode (a to add, v for view mode, g to generate, c to change master, h for help and q for quit): ")

    if mode == "q":
        break

    if mode == "v":
        view()

    elif mode == "a":
        add()
    
    elif mode == "g":
        typen = input("which password type(1, 2, 3 or 4): ")
        generate(typen)

    elif mode == "c":
        changeMaster()
    
    elif mode == "h":
        help()