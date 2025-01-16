def max_dominoes(a, b, c, d):
    return max((a // c) * (b // d), (a // d) * (b // c))


a = 10
b = 6
c = 3
d = 2

max_count = max_dominoes(a, b, c, d)
print(max_count)
