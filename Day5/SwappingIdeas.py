a, b, c, d, e, f, g, h= 1, 2, 3, 4, 5, 6, 7, 8
# Swapping using method - 1:
print('Method 1: ')
print(a, b)
a, b = b, a 
print(a, b)
# Swapping using method - 2:
print('Method 2: ')
print(c, d)
temp = c
c = d
d = temp
print(c, d)
# Swapping using method - 3:
print('Method 3: ')
print(e, f)
e = e + f
f = e - f
e = e - f
print(e, f)
# Swapping using method - 4:
print('Method 4: ')
print(g, h)
g = g + h - (h := g)
print(g, h)

