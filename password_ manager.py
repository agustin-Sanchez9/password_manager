import os
from password_generator import *
from cryptography.fernet import Fernet

# only uncomment if you want to overwrite the masterKey.key file with a new one
"""
def writeMasterKey():
    masterKey = Fernet.generate_key()
    with open("masterKey.key", "wb") as f:
        f.write(masterKey)

writeMasterKey()
"""

def loadMasterKey():
    file = open("masterKey.key", "rb")
    masterKey = file.read()
    file.close()
    return masterKey

mKey = loadMasterKey()
mFer = Fernet(mKey)



if not os.path.exists("master_password.txt"):
    master = input("Create your master password: ")
    with open("master_password.txt", "w") as f:
        f.write(mFer.encrypt(master.encode()).decode())

with open("master_password.txt" , "r") as masterfile:
    masterPwd = masterfile.read()
    masterPwd = mFer.decrypt(masterPwd.encode()).decode()

correctMaster = False

while not correctMaster:
    inputMaster = input("Enter the master password: ")
    if inputMaster == masterPwd:
        correctMaster = True
    else:
        print("incorrect password, try again")

# only uncommet if you want to overwrite the key.key file with a new one
"""
def writeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)

writeKey()
"""

def loadKey():
    file = open("key.key", "rb")
    key0 = file.read()
    file.close()
    return key0

key = loadKey()
fer = Fernet(key)

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            title, user, password = data.split("|")
            print("|| Title:",title,"|| User:", user, "|| Password:", fer.decrypt(password.encode()).decode())

def add():
    title = input("-> Title: ")
    name = input("-> User name: ")
    pwd = input("-> Password: ")

    with open("password.txt", "a") as f:
        f.write(title + "|" + name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def generate(typen):
    if typen == "1":
        print("->    " + type1)
        use = input("Do you want to use the password (y/n): ")
        if use == "y":
            title = input("-> Title: ")
            name = input("-> User name: ")
            with open("password.txt", "a") as f:
                f.write(title + "|" + name + "|" + fer.encrypt(type1.encode()).decode() + "\n")
    elif typen == "2":
        print("->    " + type2)
        use = input("Do you want to use the password (y/n): ")
        if use == "y":
            title = input("-> Title: ")
            name = input("-> User name: ")
            with open("password.txt", "a") as f:
                f.write(title + "|" + name + "|" + fer.encrypt(type2.encode()).decode() + "\n")
    elif typen == "3":
        print("->    " + type3)
        use = input("Do you want to use the password (y/n): ")
        if use == "y":
            title = input("-> Title: ")
            name = input("-> User name: ")
            with open("password.txt", "a") as f:
                f.write(title + "|" + name + "|" + fer.encrypt(type3.encode()).decode() + "\n")
    elif typen == "4":
        print("->    " + type4)
        use = input("Do you want to use the password (y/n): ")
        if use == "y":
            title = input("-> Title: ")
            name = input("-> User name: ")
            with open("password.txt", "a") as f:
                f.write(title + "|" + name + "|" + fer.encrypt(type4.encode()).decode() + "\n")

def changeMaster():
    newMaster = input("-> Write the new master password: ")
    with open("master_password.txt", "w") as f:
        f.write(mFer.encrypt(newMaster.encode()).decode())


def help():
    print("-> 0 will represent a two digit number, for example: 12")
    print("-> word will represent a word from english, for example: Listen")
    print("-> ? will represent a special character, for example: ( or =")
    print("-> type 1 password: 0word0word0")
    print("-> type 2 password: 0word0word??")
    print("-> type 3 password: 00word?word??")
    print("-> type 4 password: its an all random password using a combination of any ascii symbols")


while True:
    mode = input("Select mode (a to add, v for view mode, g to generate, c to change master, h for help and q for quit): ")

    if mode == "q":
        break

    if mode == "v":
        view()

    elif mode == "a":
        add()
    
    elif mode == "g":
        typen = input("-> Choose the password type(1, 2, 3, 4 or any to go back): ")
        generate(typen)

    elif mode == "c":
        changeMaster()
    
    elif mode == "h":
        help()