import random
import string

wordsSelected = ["Please","Love","Home","Friend","School","Time","Serius","Palace","Action","Sleep","Dream",
"Dance","Read","Listen","Write","Taste","Touch","Happy","Angry","Brave","Scared","Honest","Strong","Clean",
"Heavy","Cold","Simple","Closed","Smart","Lazy","Dumb","Wise","Polite","Rude","Humble","Modest","Nervous",
"Bored","Creative","Patient","Sincere","Tasty","Unique","Alert","Fake","Explore","Ignore","Blame","Consume",
"Conform","Resist","Damage","Repel","Dispose","Include","Generate","Future"]

specialsSelected = [".",",","?",")","(","+","-","=","#","%","/"]

# 0 = number, xxx = words, ? = special character
# type 1 = 00xxx00xxx00
def pwdType_1():
    words = wordsSelected
    digits = string.digits

    pwd1 = ""
    newStep = random.choice(digits)
    pwd1 += newStep
    newStep = random.choice(digits)
    pwd1 += newStep
    newStep = random.choice(words)
    pwd1 += newStep
    newStep = random.choice(digits)
    pwd1 += newStep
    newStep = random.choice(digits)
    pwd1 += newStep
    newStep = random.choice(words)
    pwd1 += newStep
    newStep = random.choice(digits)
    pwd1 += newStep
    newStep = random.choice(digits)
    pwd1 += newStep

    return pwd1

type1 = pwdType_1()

# type 2 = 00xxx00xxx??
def pwdType_2():
    words = wordsSelected
    digits = string.digits
    specialChars = specialsSelected

    pwd2 = ""
    newStep = random.choice(digits)
    pwd2 += newStep
    newStep = random.choice(digits)
    pwd2 += newStep
    newStep = random.choice(words)
    pwd2 += newStep
    newStep = random.choice(digits)
    pwd2 += newStep
    newStep = random.choice(digits)
    pwd2 += newStep
    newStep = random.choice(words)
    pwd2 += newStep
    newStep = random.choice(specialChars)
    pwd2 += newStep
    newStep = random.choice(specialChars)
    pwd2 += newStep

    return pwd2

type2 = pwdType_2()

# type 3 = 0000xxx?xxx??
def pwdType_3():
    words = wordsSelected
    digits = string.digits
    specialChars = specialsSelected

    pwd3 = ""
    newStep = random.choice(digits)
    pwd3 += newStep
    newStep = random.choice(digits)
    pwd3 += newStep
    newStep = random.choice(digits)
    pwd3 += newStep
    newStep = random.choice(digits)
    pwd3 += newStep
    newStep = random.choice(words)
    pwd3 += newStep
    newStep = random.choice(specialChars)
    pwd3 += newStep
    newStep = random.choice(words)
    pwd3 += newStep
    newStep = random.choice(specialChars)
    pwd3 += newStep
    newStep = random.choice(specialChars)
    pwd3 += newStep

    return pwd3
    
type3 = pwdType_3()

# type 4 = all random
def pwdType_4(min_length,number=True,special=True):
    letters = string.ascii_letters
    digits = string.digits
    specialChars = string.punctuation

    characters = letters
    if number:
        characters += digits
    if special:
        characters += specialChars

    pwd4 = ""
    meetsCriteria = False
    hasNumber = False
    hasSpecial = False

    while not meetsCriteria or len(pwd4) < min_length:
        newChar = random.choice(characters)
        pwd4 += newChar

        if newChar in digits:
            hasNumber = True
        elif newChar in specialChars:
            hasSpecial = True
        
        meetsCriteria = True
        if number:
            meetsCriteria = hasNumber
        if special:
            meetsCriteria = meetsCriteria and hasSpecial
    
    return pwd4

type4 = pwdType_4(15)