import os
from password_generator import *


if not os.path.exists("master_password.txt"):
    master = input("create your master: ")
    with open("master_password.txt", "w") as f:
        f.write(master)

with open("master_password.txt" , "r") as masterfile:
    masterPwd = masterfile.read()

correctMaster = False

while not correctMaster:
    inputMaster = input("enter the master pwd: ")
    if inputMaster == masterPwd:
        correctMaster = True
    else:
        print("incorrect master, try again")

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            print(line.rstrip())

def add():
    name = input("name: ")
    pwd = input("pwd: ")

    with open("password.txt", "a") as f:
        f.write("name: " + name + " , pwd: " + pwd + "\n")

def generate(typen):
    if typen == "type1":
        print(type1)
        use = input("do you want to use the pwd: ")
        if use == "yes":
            name = input("name: ")
            with open("password.txt", "a") as f:
                f.write("name: " + name + " , pwd: " + type1 + "\n")
    elif typen == "type2":
        print(type2)
        use = input("do you want to use the pwd: ")
        if use == "yes":
            name = input("name: ")
            with open("password.txt", "a") as f:
                f.write("name: " + name + " , pwd: " + type2 + "\n")
    elif typen == "type3":
        print(type3)
        use = input("do you want to use the pwd: ")
        if use == "yes":
            name = input("name: ")
            with open("password.txt", "a") as f:
                f.write("name: " + name + " , pwd: " + type3 + "\n")
    elif typen == "type4":
        print(type4)
        use = input("do you want to use the pwd: ")
        if use == "yes":
            name = input("name: ")
            with open("password.txt", "a") as f:
                f.write("name: " + name + " , pwd: " + type4 + "\n")

def changeMaster():
    newMaster = input("create the new master: ")
    with open("master_password.txt", "w") as f:
        f.write(newMaster)


while True:
    mode = input("mode: ")

    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()
    
    elif mode == "generate":
        typen = input("which pwd type: ")
        generate(typen)

    elif mode == "change master":
        changeMaster()