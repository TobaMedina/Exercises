# Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

class RomanNumerals:
    @staticmethod
    def to_roman(val):
        roman_numerals = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        roman = ''
        for value, symbol in roman_numerals.items():
            while val >= value:
                roman += symbol
                val -= value
        return roman

    @staticmethod
    def from_roman(roman_num):
        roman_numerals = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        result = 0
        i = 0
        while i < len(roman_num):
            current_value = roman_numerals[roman_num[i]]
            if i + 1 < len(roman_num) and roman_numerals[roman_num[i + 1]] > current_value:
                result += roman_numerals[roman_num[i + 1]] - current_value
                i += 2
            else:
                result += current_value
                i += 1
        return result


print(RomanNumerals.to_roman(2000))
print(RomanNumerals.to_roman(1666))
print(RomanNumerals.to_roman(1000))
print(RomanNumerals.to_roman(400))
print(RomanNumerals.to_roman(90))
print(RomanNumerals.to_roman(40))
print(RomanNumerals.to_roman(1))

print(RomanNumerals.from_roman("MM"))
print(RomanNumerals.from_roman("MDCLXVI"))
print(RomanNumerals.from_roman("M"))
print(RomanNumerals.from_roman("CD"))
print(RomanNumerals.from_roman("XC"))
print(RomanNumerals.from_roman("XL"))
print(RomanNumerals.from_roman("I"))
