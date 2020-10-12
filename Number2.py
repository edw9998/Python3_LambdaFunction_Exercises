from random import randint

def random_multiplication(n):
    m = randint(1, 100)         # Multiply int(input()) with a random integer between 1 and 100 --> Both are included.                  
    return n * m                

x = int(input("Enter Multiplicand for random integer: "))   # Enter a multiplicand to be multiplied with the generated randint.    
print("Result =", random_multiplication(x))                 # Return multiplication result.




