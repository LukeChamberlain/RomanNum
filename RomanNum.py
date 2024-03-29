def parseRoman(roman):
    romanNumerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    parsed = [romanNumerals.get(char, -1) for char in roman]
    if -1 in parsed:
        raise ValueError("Invalid Roman numeral")
    return parsed

def convert(parsedRoman):
    A = 0
    B = 0
    for value in parsedRoman:
        if value > B:
            A += value - 2 * B
        else:
            A += value
        B = value
    return A

def parseBack(nums):
    romanNumerals = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    roman = ""
    for num in nums:
        for key in sorted(romanNumerals.keys(), reverse = True):
            while num >= key:
                roman += romanNumerals[key]
                num -= key
    return roman

        
try:
    romanNumeral = input("Please type a Roman Numeral (XVI, IIVL, XLIV, etc): ").upper()
    parsedRoman = parseRoman(romanNumeral)
    print("Number: ", convert(parsedRoman))
    print("Roman Numeral: ", parseBack(parsedRoman))
except ValueError as e:
    print(e)