# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
# we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.

def dig_pow(n, p):
    n_str = str(n)
    sum_p = 0
    for digit in n_str:
        sum_p += int(digit) ** p
        p += 1

    if sum_p % n == 0:
        k = sum_p / n
        if k > 0:
            return k
    return -1


check = dig_pow(46288, 3)
print(check)
