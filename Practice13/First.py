def sum_of_first_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_first_n(n - 1)

n = 8
result = sum_of_first_n(n)
print("Sum of the first", n, "numbers is:", result)
