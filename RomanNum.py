RomanNum = input("Please type a roman Numeral (XVI, IIVL, XLIV, etc): ")
RomanNumSplit = list(RomanNum)
# def Convert(RomanNumSplit):
count = len(RomanNumSplit)
index = 0
print(len(RomanNumSplit))
def Convert(RomanNumSplit):
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
        
Convert(RomanNumSplit)
print(RomanNumSplit)
        
# Convert(RomanNumSplit)
# print(RomanNumSplit)

