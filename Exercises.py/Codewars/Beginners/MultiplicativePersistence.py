# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

def persistence(n):
    count = 0
    while n >= 10:
        digits = [int(digit) for digit in str(n)]
        n = 1
        for digit in digits:
            n *= digit
        count += 1
    return count


check = persistence(39)
print(check)
