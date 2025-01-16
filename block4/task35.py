def max_rectangles(a, b, c, d):

    rects_along_long_side = (a // c) * (b // d)
    rects_along_short_side = (a // d) * (b // c)

    return max(rects_along_long_side, rects_along_short_side)


a = 20
b = 10
c = 8
d = 4
max_count = max_rectangles(a, b, c, d)
print(max_count)
