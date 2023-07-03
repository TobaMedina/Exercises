# Given the triangle of consecutive odd numbers. Calculate the sum of the numbers in the nth row of this triangle
def row_sum_odd_numbers(n):
    row_start = 1
    for i in range(2, n+1):
        row_start += 2 * (i - 1)
    row_sum = sum(range(row_start, row_start + (2 * n), 2))
    return row_sum
# def row_sum_odd_numbers(n):
#   return n ** 3


check = row_sum_odd_numbers(4)
print(check)
