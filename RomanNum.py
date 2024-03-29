
intial = input("Please type a roman Numeral (XVI, IIVL, XLIV, etc): ")
RomanNumSplit = list(intial)
count = len(RomanNumSplit)

def RomToNum(RomanNumSplit):
    index = 0
    while index < len(RomanNumSplit):
        if RomanNumSplit[index] == "I":
            RomanNumSplit[index] = 1
            index += 1
        elif RomanNumSplit[index] == "V":
            RomanNumSplit[index] = 5
            index += 1
        elif RomanNumSplit[index] == "X":
            RomanNumSplit[index] = 10
            index += 1
        elif RomanNumSplit[index] == "L":
            RomanNumSplit[index] = 50
            index += 1
        elif RomanNumSplit[index] == "C":
            RomanNumSplit[index] = 100
            index += 1
        elif RomanNumSplit[index] == "D":
            RomanNumSplit[index] = 500
            index += 1
        elif RomanNumSplit[index] == "M":
            RomanNumSplit[index] = 1000
            index += 1
        else:
            print("Please input a valid Roman Numeral")
            break
def RuleOne(RomanNumSplit):
    val = 1
    while True:
        while val >= len(RomanNumSplit):
            if RomanNumSplit[0] >= RomanNumSplit[val]:
                val += 1
                return True
            else:
                return False
        return sum(RomanNumSplit)

RomToNum(RomanNumSplit)
print(RuleOne(RomanNumSplit))


