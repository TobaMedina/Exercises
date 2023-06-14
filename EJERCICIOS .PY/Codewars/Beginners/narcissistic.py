def narcissistic(value):
    valueStr = str(value)
    numDigits = len(valueStr)
    suma = sum(int(digit) ** numDigits for digit in valueStr)
    return suma == value


check = narcissistic(153)
print(check)
