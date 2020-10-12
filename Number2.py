from random import randint

def random_multiplication(n):
    global m
    m = randint(1, 100)
    return n * m

x = int(input("Enter Multiplicand for random integer: "))
print("Result =", random_multiplication(x))




