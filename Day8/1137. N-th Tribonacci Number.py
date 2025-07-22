def tribonacci(n):
    a = 0
    b = 1
    c = 1
    for item in range(n):
        temp_for_a = a
        temp_for_b = b
        a = b
        b = c
        c = temp_for_a + temp_for_b + c
    return a

# No need to define the base cases separately, like:
# if n == 0:
#     return a
# elif n == 1:
#     return b
# elif n == 2:
#     return c
# else:
#      for item in range(n):
#          ---- Further code ----
            
# Because these base cases are also being handled
# as for n == 0 the for loop will not be executed
# becaues it will have nothing to iterate upon, since
# range(0) gives nothing to iterate upon.
# Furthermore the n ==1 and n == 2 are handled by the 
# value of b being assigned to a.
def solve():
    n = 4
    print(tribonacci(n))

if __name__ == '__main__':
    solve()