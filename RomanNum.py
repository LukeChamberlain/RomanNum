def parseRoman(roman):
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    parsed = [roman_numerals.get(char, -1) for char in roman]
    if -1 in parsed:
        raise ValueError("Invalid Roman numeral")
    return parsed

def convert(parsed_roman):
    A = 0
    B = 0
    for value in parsed_roman:
        if value > B:
            A += value - 2 * B
        else:
            A += value
        B = value
    return A

try:
    roman_numeral = input("Please type a Roman Numeral (XVI, IIVL, XLIV, etc): ").upper()
    parsed_roman = parseRoman(roman_numeral)
    decimal_value = convert(parsed_roman)
    print("Value Number:", decimal_value)
except ValueError as e:
    print(e)