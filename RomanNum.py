#Takes the input in the form of roman numerals and converts it to numbers
def parseRoman(roman):
    #parses the roman numeral and converts it to corresponding number value by using a dictionary
    romanNumerals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    #looks up corresponding value in the diction if the value isn't found
    #then it returns -1 which then raises the error that it is an invalid roman numeral
    parsed = [romanNumerals.get(char, -1) for char in roman]
    if -1 in parsed:
        raise ValueError("Invalid Roman numeral")
    return parsed

#Takes the number and applies the roman numeral rules to get the specific number
def convert(parsedRoman):
    A = 0
    B = 0
    for value in parsedRoman:
        #If the current value is greater than the previous value (B), it subtracts 
        #twice the previous value (2 * B) from the current value before adding it to A
        if value > B:
            A += value - 2 * B
        else:
        #If not then it adds the value to A
            A += value
        B = value
    return A

def parseBack(nums):
    #Using dictionary to find corresponding number to the roman numeral
    romanNumerals = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    roman = ""
    
    # This is a loop that iterates through each decimal number in the input list nums.
    for num in nums:
        #This nested loop iterates through the keys of the romanNumerals dictionary in descending order. 
        #Sorting the keys in reverse ensures that we start with the largest possible Roman numeral value.
        for key in sorted(romanNumerals.keys(), reverse = True):
            #This loop runs as long as the current decimal number num is greater than or equal to the current key
            while num >= key:
                #Adds the value to the roman string
                roman += romanNumerals[key]
                num -= key
    return roman

        
romanNumeral = input("Please type a Roman Numeral (XVI, IIVL, XLIV, etc): ").upper()
parsedRoman = parseRoman(romanNumeral)
print("Number: ", convert(parsedRoman))
print("Roman Numeral: ", parseBack(parsedRoman))
